from django.http import HttpResponse
from .models import Customer,Order
from django.db.models import Sum,Avg,Count
from django.db.models import F


def index(request):
    #------------------- 'Values' function -----------------------------

    #c1=Customer.objects.values()
    #print(c1) # returns a list of dicts <QuerySet [{'customer_id': 1, 'name': 'utsav'}, {'customer_id': 2, 'name': 'poushali'}, {'customer_id': 3, 'name': 'mritunjay'}]>
#
    #for i in c1:
    #    print(i) # can iterate each of dicts
    
    #c1=Customer.objects.filter(customer_id=2).values()
    #print(c1) # <QuerySet [{'customer_id': 2, 'name': 'poushali'}]>

    #c1=Customer.objects.filter(name__startswith='u').values()
    #print(c1) # <QuerySet [{'customer_id': 1, 'name': 'utsav'}]>

    #c1=Customer.objects.filter(name__endswith='y').values()
    #print(c1) # <QuerySet [{'customer_id': 3, 'name': 'mritunjay'}]>

    #c1=Customer.objects.filter(name__contains='uts').values() # contains allows to match substring
    #print(c1) # <QuerySet [{'customer_id': 1, 'name': 'utsav'}]>


    #------------------------- 'Values-list' function --------------------------------

    #c1=Customer.objects.values_list()
    #print(c1) # returns a list of tuples <QuerySet [(1, 'utsav'), (2, 'poushali'), (3, 'mritunjay')]>

    #c1=Customer.objects.values_list(flat=True)
    #print(c1) # by default returns a list primary key's <QuerySet [1, 2, 3]>

    #c1=Customer.objects.values_list('name',flat=True)
    #print(c1) # returns a list of names <QuerySet ['utsav', 'poushali', 'mritunjay']>

    # --------------------   Aggregates ---------------------------

    """
    This method is used to perform an aggregate function 
    (like SUM, COUNT, AVG, MIN, or MAX) on a queryset. 
    It returns a dictionary of aggregate values. 
    It collapses the queryset into a single value based 
    on the aggregation function specified.
    """

    # Find Total order amount for a customer
    #res=Order.objects.filter(customer__customer_id=1).aggregate(total_amount=Sum('amount')) # customer__customer_id=1 means customer field of Order table which is a foreign key and refers to Customer Table and __customer_id means customer_id field of that Customer Table.
    #print(res)
#
    ## Find Total order quant for a customer
    #res=Order.objects.filter(customer__customer_id=1).aggregate(total_quant=Sum('quant'))
    #print(res)
#
    ## Find Average order amount for a customer
    #res=Order.objects.filter(customer__customer_id=1).aggregate(avg_amount=Avg('amount')) 
    #print(res)
#
    ## Find Total number of a customer
    #res=Order.objects.filter(customer__customer_id=1).count()
    #print(res)


    # --------------------- Annotate -----------------------

    """
    In Django, annotate() is a QuerySet method that allows you 
    to add annotations to each item in the queryset.
    These annotations can be aggregations, calculations, 
    or any other type of additional data you want to attach to each item.
    The result is that each item in the queryset will have an additional 
    attribute, which is the result of the annotation.
    """

    # Basic Annotation: Adding a calculated field to each Order object.
    orders_with_total = Order.objects.annotate(
        total_amount=F('quant') * F('amount')
    )
    for i in orders_with_total:
        """
        utsav   40
        utsav   270
        mritunjay   4950
        """
        #print(i.customer.name,' ',i.total_amount)
    

    orders_with_total = Order.objects.filter(customer__customer_id=1).annotate(
        total_amount=F('quant') * F('amount')
    )
    for i in orders_with_total:
        """
        utsav   40
        utsav   270
        """
        #print(i.customer.name,' ',i.total_amount)
    
    customers_with_total_orders = Order.objects.annotate(
        total_orders=Sum('quant')
    )
    for i in customers_with_total_orders:
        """
        utsav   2
        utsav   3
        mritunjay   9
        """
        #print(i.customer.name,' ',i.total_orders)
    


    return HttpResponse('<h4>Hello!</h4>')
