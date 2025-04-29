

from components.document_loader import document_loader





def test_loader(urls : list[str]):
    result = document_loader.invoke(urls)
    return result

result = test_loader(["https://en.wikipedia.org/wiki/LangChain"])
print(len(result))
