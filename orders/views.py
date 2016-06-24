from django.http import HttpResponse





def index(request):

    from lxml import etree
    import requests
    from orders.models import Order
    Order.objects.all().delete()
    xml = requests.get("http://test.lengow.io/orders-test.xml")

    tree = etree.fromstring(xml.content)
    for order in tree.xpath("/statistics/orders/order"):
      o = Order()
      for child in order:
        setattr(o, child.tag, child.text)
      o.save()
    return HttpResponse("L'importation de orders-test.xml s'est déroulée avec succès. <br /> <a href='/api/orders/'>consulter les données</a>")
