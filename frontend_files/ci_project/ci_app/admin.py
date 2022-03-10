from django.contrib import admin
from ci_app.models.team_member import TeamMember
from ci_app.models.product import Product
from ci_app.models.customer_order import CustomerOrder
from ci_app.models.customer_order_item import CustomerOrderItem
from ci_app.models.customer import Customer
# Register your models here.

admin.site.register(TeamMember)
admin.site.register(Product)
admin.site.register(CustomerOrder)
admin.site.register(CustomerOrderItem)
admin.site.register(Customer) 
