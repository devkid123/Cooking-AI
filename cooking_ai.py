from google import genai
from google.genai import types
import os
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font(fname='LucidaGrande.ttf')
pdf.set_font("LucidaGrande", size=12)

client = genai.Client(api_key=os.environ["COOKING_AI_KEY"])

food = input("Enter a food item >> ")
food_formatted = food.replace(' ','+')
print("\nGenerating response......This may take a while")
response = client.models.generate_content(
    model='models/gemini-2.0-flash',

    contents=f'Generate a step-by-step, easy-to-follow recipe for {food}. Include a list of ingredients with precise measurements, clear cooking instructions, estimated preparation and cooking time, serving size, and any helpful tips. Ensure the instructions are concise, beginner-friendly, and well-structured. Take reference from this website, read it well and enhance its recipe: https://www.seriouseats.com/search?q={food_formatted}'
)

print("\nGenerating PDF......")
pdf.multi_cell(0,10,response.text)
pdf.output(f"Recipe_for_{food}.pdf")
print("Made a PDF")

'''
response = client.models.generate_content(

    model='tunedModels/cookingaimodel-fuisy138je2',
    contents='Generate a step-by-step, easy-to-follow recipe for chicken biryani'
)
print("\nGenerating PDF......")
pdf.multi_cell(0,10,response.text)
pdf.output(f"Recipe_for_shitty_chicken_biryani.pdf")
print("Made a PDF")

'''
