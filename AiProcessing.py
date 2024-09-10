import os
import json
import cohere
from rich.progress import track
from rich.console import Console
from datetime import datetime

console = Console()

class AiProcessing:
    def __init__(self, celigo_ai_dir):
        self.celigo_ai_dir = celigo_ai_dir
        self.output_directory = os.path.join(celigo_ai_dir, "DocumentResources")
        self.cohere_api_key = os.getenv("COHERE_API_KEY")
        self.log_file = os.path.join(
            self.celigo_ai_dir,
            f"ai_processing_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
        )

        if self.cohere_api_key:
            console.print("[green]API key is set.[/green]")
            self.client = cohere.Client(self.cohere_api_key)
        else:
            console.print(
                "[red]Error: COHERE_API_KEY environment variable not found.[/red]"
            )
            exit(1)

        # Ensure output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def log_message(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"[[{level}] " #{timestamp}] ,{message}
        console.print(formatted_message)
        with open(self.log_file, "a") as f:
            f.write(formatted_message + "\n")

    def process_descriptions(self):
        for folder in ["exports", "imports"]:
            folder_path = os.path.join(self.celigo_ai_dir, "extracted", folder)
            if os.path.exists(folder_path):
                for filename in track(
                    os.listdir(folder_path),
                    description=f"Processing {folder}...",
                ):
                    if filename.endswith(".json"):
                        filepath = os.path.join(folder_path, filename)
                        self.process_json_file(filepath)
            else:
                self.log_message(
                    f"Warning: Folder not found: {folder_path}", level="WARNING"
                )

    def process_json_file(self, filepath):
        try:
            with open(filepath, "r") as f:
                json_data = json.load(f)

            preamble = (
                "You are responsible for documenting Celigo integration flows clearly and concisely. Your goal is to provide clients with comprehensive, easy-to-understand documentation that outlines the flow name, filters used, mappings (as markdown table with all the info), and lookups. Your documentation should follow a structured format, using markdown syntax for docx, and be tailored to the client’s needs. "
              
            )

            prompt = (
                f"{json.dumps(json_data, indent=2)}\n\n"
            )

            response = self.client.chat(
                model="command-r-plus-08-2024",
                message=prompt,
                preamble=preamble,
                temperature=0.3,  
                 chat_history=[], 
            )

            cohere_response = response.text

            # Save Response to DocumentResources Folder
            item_id = os.path.basename(filepath)[-24:-5]
            output_filename = os.path.join(
                self.output_directory, f"{item_id}_Description.md"
            )

            with open(output_filename, "w") as outfile:
                outfile.write(cohere_response)

            #self.log_message(f"Response saved to: {output_filename}")

        except Exception as e:
            self.log_message(
                f"Error processing {filepath}: {str(e)}", level="ERROR"
            )

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    celigo_ai_dir = os.path.join(base_dir, "CeligoAI")
    ai_processor = AiProcessing(celigo_ai_dir)
    ai_processor.process_descriptions()