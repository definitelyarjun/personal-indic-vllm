from sarvamai import SarvamAI
from sarvamai.play import save
from dotenv import load_dotenv
import os
import gradio as gr

load_dotenv()
api_key = os.getenv("SARVAM_API_KEY")

client = SarvamAI(
  api_subscription_key=f'{api_key}',
)

def transcribe_audio(file_path):
  
  response_stt = client.speech_to_text.transcribe(
    file=open(file_path, "rb"),
    model="saarika:v2",
    language_code="ml-IN"
  )
  
  response_llm = client.chat.completions(messages=[
    {"role": "user", "content": response_stt.transcript},
  ])
  #return response_llm.choices[0].message.content
  
  audio = client.text_to_speech.convert(
      target_language_code="ml-IN",
      text=response_llm.choices[0].message.content,
      model="bulbul:v2",
      speaker="manisha"
  )
  output_path = "output1.wav"
  save(audio, output_path)
  return output_path


Interface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(sources=["microphone"], type="filepath", label="Speak into the microphone"),
    outputs=gr.Audio(label="Generated Response", type="filepath")
)

Interface.launch()

#NEXT STEP - Save audiofiles in a different directory and dynamically assign names to them using datetime.