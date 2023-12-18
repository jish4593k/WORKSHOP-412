import os
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from .generators import PDFGenerator
from .settings import pdf_settings
from .utils import get_random_filename

import torch
import tensorflow as tf
import seaborn as sns
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

def render_pdf(filename, request, template_name, context=None, content_type=None, status=None, using=None, options={}):
    
    content = loader.render_to_string(template_name, context, request, using=using)

    # Check if the request includes 'html' parameter, and return HTML content if present
    if request.GET.get('html'):
        return HttpResponse(content, content_type, status)

   
    html_key = get_random_filename(20)
    html_filename = f'{html_key}.html'
    html_file_path = os.path.join(pdf_settings.TEMPLATES_DIR, html_filename)
    
    with open(html_file_path, 'w') as f:
        f.write(content)

   
    relative_url = reverse('pdf_generator:pdf_html', kwargs={'html_key': html_key})
    url = request.build_absolute_uri(relative_url)

    pdf = PDFGenerator(url, **options)

   pe
    torch_tensor = torch.randn(3, 3)
    print("PyTorch Tensor Shape:", torch_tensor.shape)

   
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    print("Keras Model Summary:")
    model.summary()

    
    sns.set()
    x = [1, 2, 3, 4, 5]
    y = [10, 15, 7, 12, 5]
    plt.plot(x, y)
    plt.title('Seaborn Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

  
    root = tk.Tk()
    root.title("Django PDF Generator GUI")

    def draw_pdf():
        img_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image files", "*.jpg;*.png")])
        if not img_path:
            return

    button = tk.Button(root, text="Draw PDF", command=draw_pdf)
    button.pack(pady=20)

    root.mainloop()

    # Return the HTTP response for the generated PDF
    return pdf.get_http_response(filename)
