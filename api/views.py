import os
from django.shortcuts import render 
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, FileResponse
from docx2pdf import convert  

class DocumentConvertAPIView(APIView):
    
    def get(self, request):
        return render(request, 'api/convert.html')
    def post(self, request):
        if 'file' not in request.FILES:
            return HttpResponse("No file uploaded", status=400)
            
        file_obj = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file_obj.name, file_obj)
        
        input_path = fs.path(filename)
        output_dir = fs.location
        
        pdf_name = f"{os.path.splitext(filename)[0]}.pdf"
        output_pdf_path = os.path.join(output_dir, pdf_name)

        try:
            convert(input_path, output_pdf_path)
            if os.path.exists(input_path):
                os.remove(input_path)
            
            response = FileResponse(open(output_pdf_path, 'rb'), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{pdf_name}"'
            return response
            
        except Exception as e:
            if os.path.exists(input_path):
                os.remove(input_path)
            if os.path.exists(output_pdf_path):
                os.remove(output_pdf_path)
            return HttpResponse(f"Conversion failed: {str(e)}", status=500)