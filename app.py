# Import necessary libraries
import gradio as gr
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from io import BytesIO
import tempfile


# Define the function to generate a word cloud from a text file
def generate_wordcloud(file):
    # Read the text file content
    with open(file.name, "r", encoding="utf-8") as f:
        text = f.read()

    # Create word cloud
    wordcloud = WordCloud(width=800, height=400, max_words=150).generate(text)

    # Plot word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.tight_layout(pad=0)

    # Save word cloud image to temporary file
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        temp_file_path = temp_file.name
        plt.savefig(temp_file_path, format='png')
    
    # Close the plot to free up resources
    plt.close()

    # Return the path to the temporary file containing the word cloud image
    return temp_file_path

# Define input and output interfaces
inputs = gr.inputs.File(label="Upload Text File")
output = gr.outputs.Image(type='filepath', label="Word Cloud")  

# Create and launch the Gradio interface
grapp = gr.Interface(
    generate_wordcloud,
    inputs=inputs,
    outputs=output,
    title="Text File Word Cloud",
    description="Upload a text file to generate a word cloud from its contents.",
    allow_flagging=False
)


# Launch the interface on a specific server port
grapp.launch(server_port=9087)





