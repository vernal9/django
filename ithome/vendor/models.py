from django.db import models

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

# Create your models here.
class Vendor(models.Model):
	vendor_name = models.CharField(max_length = 20) # 攤販的名稱
	store_name = models.CharField(max_length = 10) # 攤販店家的名稱
	phone_number = models.CharField(max_length = 20) # 攤販的電話號碼
	address = models.CharField(max_length = 100) # 攤販的地址

	# 覆寫 __str__
	def __str__(self):
		return self.vendor_name

	def get_absolute_url(self):
		return reverse("vendors:vendor_id", kwargs={"id": self.id})


class Food(models.Model):
	food_name = models.CharField(max_length = 30) # 食物名稱
	food_price = models.DecimalField(max_digits = 3, decimal_places=0) # 食物價錢
	food_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE) # 代表這食物是由哪一個攤販所做的

	def __str__(self):
		return self.food_name

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
	#list_display 是固定寫法,不可改寫
	list_display = [field.name for field in Vendor._meta.fields]
	#list_display = ['id', 'vendor_name', 'store_name', 'phone_number', 'address']


# 自行宣告 類別,自定價格查詢
class Morethanfifty(admin.SimpleListFilter):

	title = _('price')
	parameter_name = 'compareprice' # url最先要接的參數

	def lookups(self, request, model_admin):
		return (
			('>50',_('>50')), # 前方對應下方'>50'(也就是url的request)，第二個對應到admin顯示的文字
			('<=50',_('<=50')),
		)
    # 定義查詢時的過濾條件
	def queryset(self, request, queryset):
		if self.value() == '>50':
			return queryset.filter(food_price__gt=50)
		if self.value() == '<=50':
			return queryset.filter(food_price__lte=50)


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Food._meta.fields]
	# 過濾 price_name
    list_filter = (Morethanfifty,)
	# 顯示可編輯欄位
    fields = ['food_price']
    # Search field
    search_fields = ('food_name','food_price')
    ordering = ('-food_price',) #新增 -，資料改為 由大到小 排序