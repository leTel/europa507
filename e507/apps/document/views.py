from django.shortcuts import render

import e507.apps.document.models

def document_view(request):
    documents = e507.apps.document.models.Document.objects.all()
    return render(request, 'document/list.html', {
        'documents': documents
    })


def document_detail_view(request, doc_id):
    doc = e507.apps.document.models.Document.objects.get(id=doc_id)
    return render(request, 'document/document.html', {
        'doc': doc
    })

