# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CbdCollectGoods(models.Model):
    collect_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_collect_goods'


class CbdHistory(models.Model):
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_history'


class CbdOrder(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    order_no = models.CharField(max_length=40)
    order_time = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.BigIntegerField()
    address_id = models.IntegerField()
    pay_state = models.PositiveIntegerField()
    payment_id = models.IntegerField()
    payno = models.CharField(max_length=60)
    remark = models.TextField()
    billno = models.CharField(max_length=60)
    paytime = models.IntegerField()
    payname = models.CharField(max_length=100)
    payamount = models.DecimalField(max_digits=10, decimal_places=2)
    seller_id = models.CharField(max_length=50)
    is_process = models.PositiveIntegerField()
    order_state = models.IntegerField()
    acutaltransfee = models.DecimalField(max_digits=10, decimal_places=2)
    receiver = models.CharField(max_length=50)
    contactperson = models.CharField(max_length=50)
    receiverphone = models.CharField(max_length=50)
    receivermobile = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=50)
    consignee_name = models.CharField(max_length=50)
    consignee_id_number = models.CharField(max_length=25)
    lpcode = models.CharField(max_length=50)
    paystatus = models.IntegerField()
    orderstatus = models.IntegerField()
    transcode = models.CharField(max_length=50)
    transname = models.CharField(max_length=50)
    version = models.CharField(max_length=10)
    os = models.CharField(max_length=10)
    omsstatus = models.IntegerField()
    best_time = models.CharField(max_length=120)
    is_delete = models.IntegerField()
    is_invoice = models.IntegerField()
    invoice_title = models.CharField(max_length=255)
    updatetime = models.IntegerField()
    share_count = models.IntegerField()
    share_reward = models.DecimalField(max_digits=10, decimal_places=2)
    reduction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    close_time = models.PositiveIntegerField()
    bank_code = models.CharField(max_length=10)
    tran_ischeck = models.IntegerField()
    coin = models.DecimalField(max_digits=10, decimal_places=2)
    bundling_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bunding_text = models.TextField()
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    original_amount = models.DecimalField(max_digits=10, decimal_places=0)
    isproxypay = models.IntegerField(db_column='isProxyPay')  # Field name made lowercase.
    replace = models.IntegerField()
    is_send = models.IntegerField()
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2)
    app_resource = models.IntegerField()
    ka = models.PositiveIntegerField()
    shares_num = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_bargain = models.PositiveIntegerField()
    bargain_status = models.PositiveIntegerField()
    invoice_code = models.CharField(max_length=255)
    delivery_type = models.CharField(max_length=20)
    online_or_offline = models.IntegerField()
    is_vip = models.PositiveIntegerField()
    uuid = models.CharField(max_length=36)
    is_open_vip = models.IntegerField(blank=True, null=True)
    open_vip_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_group = models.PositiveIntegerField()
    fight_id = models.PositiveIntegerField()
    fight_sum = models.PositiveIntegerField()
    cut_id = models.PositiveIntegerField()
    is_newer = models.PositiveIntegerField()
    boost_id = models.IntegerField()
    shares_balance = models.DecimalField(max_digits=10, decimal_places=2)
    reward_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cbd_order'


class CbdOrderActivity(models.Model):
    id = models.BigIntegerField(primary_key=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    activity_title = models.CharField(max_length=100, blank=True, null=True)
    activity_type = models.PositiveIntegerField(blank=True, null=True)
    activity_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    special_id = models.PositiveIntegerField(blank=True, null=True)
    goods_id = models.CharField(max_length=500, blank=True, null=True)
    undertaker_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_order_activity'


class CbdOrderDetail(models.Model):
    od_id = models.BigIntegerField(primary_key=True)
    order_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=200)
    goods_no = models.CharField(max_length=50)
    spec_id = models.IntegerField()
    sku_no = models.CharField(max_length=100)
    order_state = models.IntegerField()
    detail_no = models.CharField(max_length=60)
    erp_order_no = models.CharField(max_length=50)
    transcode = models.CharField(max_length=50)
    transname = models.CharField(max_length=50)
    trans_company_code = models.CharField(max_length=50)
    transtime = models.IntegerField()
    complete_time = models.PositiveIntegerField()
    supply_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    shop_price = models.DecimalField(max_digits=10, decimal_places=2)
    flash_price = models.DecimalField(max_digits=10, decimal_places=2)
    newer_price = models.DecimalField(max_digits=10, decimal_places=2)
    taojj_price = models.DecimalField(max_digits=10, decimal_places=2)
    vip_price = models.DecimalField(max_digits=10, decimal_places=2)
    group_price = models.DecimalField(max_digits=10, decimal_places=2)
    group_number = models.PositiveIntegerField()
    num = models.IntegerField()
    discount_fee = models.DecimalField(max_digits=10, decimal_places=2)
    discount_flash_price = models.DecimalField(max_digits=10, decimal_places=2)
    fdc_self_discount = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    skusize = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    paystatus = models.IntegerField()
    orderstatus = models.IntegerField()
    supplier_id = models.IntegerField(blank=True, null=True)
    bathch = models.CharField(max_length=200)
    is_push = models.IntegerField()
    push_msg_id = models.IntegerField()
    push_error_msg = models.CharField(max_length=50)
    push_error_code = models.IntegerField()
    shop_id = models.IntegerField()
    is_delete = models.IntegerField()
    is_gift = models.IntegerField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    gift_special_id = models.PositiveIntegerField()
    is_pack = models.IntegerField()
    is_pack_goods = models.IntegerField()
    is_return = models.IntegerField()
    is_change = models.IntegerField()
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)
    crazy_coin = models.DecimalField(max_digits=10, decimal_places=2)
    money_ratio = models.DecimalField(max_digits=10, decimal_places=2)
    money_ratio_after = models.DecimalField(max_digits=10, decimal_places=2)
    sms_stock_fail_time = models.IntegerField()
    sms_deliver_fail_time = models.IntegerField()
    random_pack = models.PositiveIntegerField()
    is_random = models.PositiveIntegerField()
    return_num = models.IntegerField()
    return_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_fbs = models.IntegerField()
    fbs_version = models.CharField(max_length=10)
    coupon_price = models.DecimalField(max_digits=10, decimal_places=2)
    source_special_id = models.PositiveIntegerField()
    is_child = models.IntegerField()
    goods_type = models.IntegerField()
    is_haitao = models.PositiveIntegerField()
    rebate_proportion = models.PositiveIntegerField()
    createtime = models.IntegerField()
    shares_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_delivery = models.IntegerField()
    is_urge = models.IntegerField(blank=True, null=True)
    spec_name_one = models.CharField(max_length=40, blank=True, null=True)
    spec_name_two = models.CharField(max_length=40, blank=True, null=True)
    shares_balance = models.DecimalField(max_digits=10, decimal_places=2)
    reward_balance = models.DecimalField(max_digits=10, decimal_places=2)
    merchant_subsidy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_order_detail'


class CbdOrderDetailKa(models.Model):
    od_id = models.BigIntegerField(primary_key=True)
    order_id = models.BigIntegerField()
    detail_no = models.CharField(max_length=80)
    ka_price = models.DecimalField(max_digits=10, decimal_places=2)
    ka_amount = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.PositiveIntegerField()
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_order_detail_ka'


class CbdOrderGoodsSource(models.Model):
    od_id = models.BigIntegerField(primary_key=True)
    goods_source = models.CharField(max_length=100, blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)
    device_id = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'cbd_order_goods_source'


class CbdOrderPayname(models.Model):
    order_id = models.BigIntegerField()
    order_time = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    num = models.IntegerField()
    payname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cbd_order_payname'


class CbdOrderSupplierFreight(models.Model):
    order_id = models.BigIntegerField(blank=True, null=True)
    detail_no = models.CharField(max_length=60, blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    province = models.SmallIntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fbs_supplier_id = models.IntegerField(blank=True, null=True)
    json_freight_fee = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_order_supplier_freight'


class CbdOrderTag(models.Model):
    order_id = models.BigIntegerField()
    tag = models.CharField(max_length=30)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_order_tag'


class CbdOrderUuid(models.Model):
    order_id = models.BigIntegerField()
    order_time = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    num = models.PositiveIntegerField()
    uuid = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'cbd_order_uuid'


class CbdReturnGoods(models.Model):
    return_id = models.BigAutoField(primary_key=True)
    return_no = models.CharField(max_length=50)
    erp_return_no = models.CharField(max_length=50)
    order_id = models.BigIntegerField()
    order_no = models.CharField(max_length=40)
    order_state = models.IntegerField()
    order_time = models.IntegerField()
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=100)
    crazy_coin = models.DecimalField(max_digits=10, decimal_places=2)
    detail_no = models.CharField(max_length=50)
    od_id = models.BigIntegerField()
    erp_order_no = models.CharField(max_length=50)
    only_refund = models.IntegerField(blank=True, null=True)
    refund_type = models.PositiveIntegerField()
    refund_account = models.CharField(max_length=50)
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=255)
    goods_img = models.CharField(max_length=255)
    spec_id = models.IntegerField()
    sku_no = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    skusize = models.CharField(max_length=20)
    shop_id = models.PositiveIntegerField()
    is_fbs = models.PositiveIntegerField()
    single_price = models.DecimalField(max_digits=10, decimal_places=2)
    number = models.IntegerField()
    price_amount = models.DecimalField(max_digits=10, decimal_places=2)
    return_wealth = models.DecimalField(max_digits=10, decimal_places=2)
    return_stock = models.DecimalField(max_digits=10, decimal_places=1)
    discount_fee = models.DecimalField(max_digits=10, decimal_places=2)
    return_reason = models.PositiveIntegerField()
    return_explain = models.CharField(max_length=800)
    erp_return_reason = models.CharField(max_length=5)
    delivery_company = models.CharField(max_length=50)
    delivery_no = models.CharField(max_length=50)
    delivery_no_add_time = models.IntegerField()
    upload_delivery_no_times = models.PositiveIntegerField()
    delivery_start_time = models.IntegerField()
    delivery_end_time = models.IntegerField()
    delivery_address = models.CharField(max_length=500)
    return_consignee = models.CharField(max_length=50)
    return_mobile = models.CharField(max_length=20)
    return_address_new = models.CharField(max_length=500)
    received_time = models.IntegerField()
    return_status = models.PositiveIntegerField()
    return_app_status = models.PositiveIntegerField()
    app_verify_remark = models.CharField(max_length=500)
    is_refuse = models.PositiveIntegerField()
    refuse_reason = models.CharField(max_length=500)
    app_refuse_reason = models.CharField(max_length=500)
    is_cancel = models.PositiveIntegerField()
    push_status = models.PositiveIntegerField()
    push_error = models.CharField(max_length=500)
    version = models.CharField(max_length=10)
    os = models.CharField(max_length=10)
    app_resource = models.PositiveIntegerField()
    is_cancel_handle = models.PositiveIntegerField()
    delivery_name = models.CharField(max_length=50)
    subscribe_delivery_status = models.PositiveIntegerField()
    subscribe_delivery_remark = models.CharField(max_length=100)
    is_remind_user_to_ship = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    update_time = models.DateTimeField()
    ship_price = models.DecimalField(max_digits=10, decimal_places=2)
    other_price = models.DecimalField(max_digits=10, decimal_places=2)
    other_reason = models.CharField(max_length=40)
    cause = models.TextField(blank=True, null=True)
    goods_status = models.IntegerField(blank=True, null=True)
    spec_name_one = models.CharField(max_length=40, blank=True, null=True)
    spec_name_two = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_return_goods'


class CbdReturnImg(models.Model):
    id = models.BigAutoField(primary_key=True)
    return_id = models.BigIntegerField()
    img_url = models.CharField(max_length=200)
    save_path = models.CharField(max_length=200)
    save_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cbd_return_img'


class CbdUserAccessToken(models.Model):
    user_id = models.BigIntegerField()
    dev_id = models.CharField(max_length=60)
    os = models.CharField(max_length=10, blank=True, null=True)
    token = models.CharField(max_length=16)
    app_resource = models.IntegerField()
    last_update = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_access_token'
        unique_together = (('user_id', 'dev_id', 'app_resource'),)


class CbdUserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    address_name = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    consignee = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)
    country = models.SmallIntegerField(blank=True, null=True)
    province = models.SmallIntegerField(blank=True, null=True)
    city = models.SmallIntegerField(blank=True, null=True)
    district = models.SmallIntegerField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    tel = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    best_time = models.CharField(max_length=120, blank=True, null=True)
    default = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_address'


class CbdUsers(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    gender = models.IntegerField()
    source = models.CharField(max_length=50, blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    reg_time = models.IntegerField(blank=True, null=True)
    lastlogin_time = models.IntegerField(blank=True, null=True)
    login_num = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    other_login = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)
    account = models.CharField(max_length=100, blank=True, null=True)
    reg_ip = models.CharField(max_length=15, blank=True, null=True)
    open_num = models.IntegerField(blank=True, null=True)
    open_time = models.IntegerField(blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)
    is_action = models.IntegerField(blank=True, null=True)
    is_temai = models.PositiveIntegerField()
    referrer_mobile_number = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'cbd_users'


class CbdUsersProfile(models.Model):
    user_id = models.BigIntegerField(unique=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    add_time = models.PositiveIntegerField()
    last_update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_users_profile'


class CbdWxUsers(models.Model):
    openid = models.CharField(unique=True, max_length=100)
    user_id = models.BigIntegerField(unique=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_wx_users'
