from django.urls import path

from .views import UploadZip, PdfFileList, PdfFileDetail, PdfView, ViewHistoryList

urlpatterns = [
    path("zip_upload/", UploadZip.as_view()),
    path("", PdfFileList.as_view()),
    path("<int:pk>/", PdfFileDetail.as_view()),
    path("media/<str:pdf_name>", PdfView),
    path("view_history/", ViewHistoryList.as_view()),
]
