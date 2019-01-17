# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CbdAccess(models.Model):
    role_id = models.PositiveSmallIntegerField()
    node_id = models.PositiveSmallIntegerField()
    level = models.IntegerField()
    pid = models.SmallIntegerField()
    module = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_access'


class CbdAccessMenu(models.Model):
    role_id = models.PositiveSmallIntegerField()
    group_id = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_access_menu'


class CbdActiveChannel(models.Model):
    device_type = models.CharField(max_length=32)
    os_version = models.CharField(max_length=16)
    event_time = models.IntegerField()
    idfa = models.CharField(max_length=40)
    mac = models.CharField(max_length=64)
    android_id = models.CharField(max_length=64)
    imei = models.CharField(max_length=32)
    tdid = models.CharField(max_length=40)
    ip = models.CharField(max_length=16)
    spread_url = models.CharField(max_length=16)
    spread_name = models.CharField(max_length=32)
    ua = models.CharField(max_length=128)
    channel_name = models.CharField(max_length=32)
    active_type = models.IntegerField(blank=True, null=True)
    created_time = models.DateTimeField()
    tag = models.CharField(max_length=32)
    app_version = models.CharField(max_length=32)
    app_resource = models.IntegerField()
    is_xcx = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_active_channel'


class CbdActivePostion(models.Model):
    act_name = models.CharField(max_length=255)
    act_pic = models.CharField(max_length=255)
    act_url = models.CharField(max_length=255)
    is_issue_app = models.PositiveIntegerField()
    is_issue_wechat = models.PositiveIntegerField()
    rank = models.PositiveSmallIntegerField()
    create_user = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    issue_user = models.PositiveIntegerField()
    issue_time = models.PositiveIntegerField()
    delete_user = models.PositiveIntegerField()
    delete_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_active_postion'


class CbdActivityBasic(models.Model):
    activity_id = models.AutoField(primary_key=True)
    fbs_activity_id = models.PositiveIntegerField()
    name = models.CharField(max_length=64)
    state = models.PositiveIntegerField()
    activity_type = models.PositiveIntegerField()
    level_1 = models.PositiveIntegerField()
    level_2 = models.PositiveIntegerField()
    level_3 = models.PositiveIntegerField()
    registration_start_time = models.PositiveIntegerField()
    registration_end_time = models.PositiveIntegerField()
    sale_time = models.PositiveIntegerField()
    out_time = models.PositiveIntegerField()
    intro = models.TextField()
    goods_stock_threshold = models.PositiveIntegerField()
    creator = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()
    is_delete = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_activity_basic'


class CbdActivityCouponLog(models.Model):
    main_id = models.PositiveIntegerField()
    operator = models.CharField(max_length=30)
    operate_type = models.PositiveIntegerField()
    operate_detail = models.CharField(max_length=500)
    operate_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_activity_coupon_log'


class CbdActivityCouponMain(models.Model):
    activity_id = models.IntegerField()
    coupon_name = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    undertaker_type = models.PositiveIntegerField()
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    receive_num = models.PositiveIntegerField()
    use_num = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()
    is_deleted = models.PositiveIntegerField()
    activity_url_id = models.IntegerField(blank=True, null=True)
    range = models.IntegerField(blank=True, null=True)
    time_type = models.IntegerField(blank=True, null=True)
    time_slot = models.IntegerField(blank=True, null=True)
    is_random = models.IntegerField(blank=True, null=True)
    min_random_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_random_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    count = models.IntegerField()
    amount_unlimited = models.IntegerField(blank=True, null=True)
    no_use_full_coupon = models.PositiveIntegerField()
    no_use_vip = models.PositiveIntegerField()
    new_user_coupon_id = models.IntegerField(blank=True, null=True)
    coupon_kind = models.IntegerField(blank=True, null=True)
    give_group = models.IntegerField(blank=True, null=True)
    image_before = models.CharField(max_length=200, blank=True, null=True)
    image_after = models.CharField(max_length=200, blank=True, null=True)
    use_range = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_activity_coupon_main'


class CbdActivityGoods(models.Model):
    activity_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    is_cancel = models.IntegerField()
    is_delete = models.PositiveIntegerField()
    is_second = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_activity_goods'


class CbdActivityMain(models.Model):
    act_id = models.AutoField(primary_key=True)
    receive_num = models.PositiveIntegerField()
    act_name = models.CharField(max_length=60)
    act_type = models.PositiveIntegerField()
    act_url = models.CharField(max_length=255, blank=True, null=True)
    act_activity = models.PositiveIntegerField()
    act_author = models.PositiveIntegerField()
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    create_user = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    last_update_user = models.PositiveIntegerField()
    last_update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_activity_main'


class CbdActivityMainCoupon(models.Model):
    act_id = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    is_del = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_activity_main_coupon'


class CbdActivityMainGoods(models.Model):
    act_id = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    is_del = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_activity_main_goods'


class CbdActivityModel(models.Model):
    activity_model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=255)
    activity_top_img = models.CharField(max_length=255)
    use_coupon = models.IntegerField(blank=True, null=True)
    coupon = models.CharField(max_length=500, blank=True, null=True)
    show_more_special = models.IntegerField(blank=True, null=True)
    more_special_img = models.CharField(max_length=255, blank=True, null=True)
    more_special = models.TextField(blank=True, null=True)
    anchor_selected_bg = models.CharField(max_length=10, blank=True, null=True)
    anchor_unselected_bg = models.CharField(max_length=10, blank=True, null=True)
    anchor_selected_font_color = models.CharField(max_length=10, blank=True, null=True)
    anchor_unselected_font_color = models.CharField(max_length=10, blank=True, null=True)
    activity_bg = models.CharField(max_length=10, blank=True, null=True)
    model_page = models.CharField(max_length=300, blank=True, null=True)
    is_invalid = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    creator = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_activity_model'


class CbdActivityPageConf(models.Model):
    model_id = models.AutoField(primary_key=True)
    activity_id = models.IntegerField(unique=True)
    model_code = models.CharField(max_length=20, blank=True, null=True)
    bg_color = models.CharField(max_length=10, blank=True, null=True)
    banner_img = models.CharField(max_length=200, blank=True, null=True)
    activity_url = models.CharField(max_length=200, blank=True, null=True)
    page_title = models.CharField(max_length=20)
    operate_time = models.IntegerField(blank=True, null=True)
    last_operator = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_activity_page_conf'


class CbdActivitySpecial(models.Model):
    activity_id = models.IntegerField()
    special_id = models.IntegerField()
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_activity_special'


class CbdActtools(models.Model):
    actname = models.CharField(max_length=255)
    actkey = models.CharField(unique=True, max_length=255)
    end_time = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'cbd_acttools'


class CbdAdListCate(models.Model):
    adv_id = models.IntegerField()
    cate_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_ad_list_cate'


class CbdAdPoster(models.Model):
    position = models.CharField(max_length=100)
    channel = models.CharField(max_length=50, blank=True, null=True)
    ad_forms = models.CharField(max_length=100, blank=True, null=True)
    position_name = models.CharField(max_length=100, blank=True, null=True)
    media_fomrs = models.CharField(max_length=50, blank=True, null=True)
    ad_width = models.IntegerField(blank=True, null=True)
    ad_height = models.IntegerField(blank=True, null=True)
    maximum = models.IntegerField(blank=True, null=True)
    cate = models.IntegerField(blank=True, null=True)
    cate_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_ad_poster'


class CbdAdPosterShop(models.Model):
    position = models.CharField(max_length=100)
    channel = models.CharField(max_length=50, blank=True, null=True)
    ad_forms = models.CharField(max_length=100, blank=True, null=True)
    position_name = models.CharField(max_length=100, blank=True, null=True)
    media_fomrs = models.CharField(max_length=50, blank=True, null=True)
    ad_width = models.IntegerField(blank=True, null=True)
    ad_height = models.IntegerField(blank=True, null=True)
    maximum = models.IntegerField(blank=True, null=True)
    cate = models.IntegerField(blank=True, null=True)
    cate_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_ad_poster_shop'


class CbdAdPosterTide(models.Model):
    position = models.CharField(max_length=100)
    channel = models.CharField(max_length=50, blank=True, null=True)
    ad_forms = models.CharField(max_length=100, blank=True, null=True)
    position_name = models.CharField(max_length=100, blank=True, null=True)
    media_fomrs = models.CharField(max_length=50, blank=True, null=True)
    ad_width = models.IntegerField(blank=True, null=True)
    ad_height = models.IntegerField(blank=True, null=True)
    maximum = models.IntegerField(blank=True, null=True)
    cate = models.IntegerField(blank=True, null=True)
    cate_position = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_ad_poster_tide'


class CbdAddressErrorLog(models.Model):
    type = models.SmallIntegerField()
    content = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'cbd_address_error_log'


class CbdAdvertisements(models.Model):
    name = models.CharField(max_length=100)
    media = models.CharField(max_length=200, blank=True, null=True)
    ad_url = models.CharField(max_length=200, blank=True, null=True)
    position_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    ad_key = models.CharField(max_length=200, blank=True, null=True)
    final_edit = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    targets = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    is_app = models.IntegerField(blank=True, null=True)
    is_wap = models.IntegerField(blank=True, null=True)
    is_web = models.IntegerField(blank=True, null=True)
    app_media = models.CharField(max_length=200, blank=True, null=True)
    app_display = models.IntegerField(blank=True, null=True)
    wap_display = models.IntegerField(blank=True, null=True)
    web_display = models.IntegerField(blank=True, null=True)
    app_start_time = models.IntegerField(blank=True, null=True)
    app_end_time = models.IntegerField(blank=True, null=True)
    wap_start_time = models.IntegerField(blank=True, null=True)
    wap_end_time = models.IntegerField(blank=True, null=True)
    web_start_time = models.IntegerField(blank=True, null=True)
    web_end_time = models.IntegerField(blank=True, null=True)
    app_sort = models.IntegerField(blank=True, null=True)
    wap_sort = models.IntegerField(blank=True, null=True)
    web_sort = models.IntegerField(blank=True, null=True)
    target_type = models.CharField(max_length=30, blank=True, null=True)
    target_info = models.CharField(max_length=255, blank=True, null=True)
    notice_text = models.TextField(blank=True, null=True)
    notice_type = models.IntegerField(blank=True, null=True)
    notice_again = models.IntegerField(blank=True, null=True)
    use_type = models.IntegerField(blank=True, null=True)
    coupon_ids = models.TextField(blank=True, null=True)
    order_time_start = models.IntegerField(blank=True, null=True)
    order_time_end = models.IntegerField(blank=True, null=True)
    is_visible_app = models.IntegerField(blank=True, null=True)
    is_visible_ouch_app = models.IntegerField(blank=True, null=True)
    is_visible_dress_app = models.IntegerField(blank=True, null=True)
    is_visible_xcx = models.IntegerField(blank=True, null=True)
    is_visible_ouch = models.IntegerField(blank=True, null=True)
    is_visible_dress = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_advertisements'


class CbdAdvertisementsShop(models.Model):
    name = models.CharField(max_length=100)
    media = models.CharField(max_length=200, blank=True, null=True)
    ad_url = models.CharField(max_length=200, blank=True, null=True)
    position_id = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    ad_key = models.CharField(max_length=200, blank=True, null=True)
    final_edit = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    targets = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    is_app = models.IntegerField(blank=True, null=True)
    is_wap = models.IntegerField(blank=True, null=True)
    is_web = models.IntegerField(blank=True, null=True)
    app_media = models.CharField(max_length=200, blank=True, null=True)
    app_display = models.IntegerField(blank=True, null=True)
    wap_display = models.IntegerField(blank=True, null=True)
    web_display = models.IntegerField(blank=True, null=True)
    app_start_time = models.IntegerField(blank=True, null=True)
    app_end_time = models.IntegerField(blank=True, null=True)
    wap_start_time = models.IntegerField(blank=True, null=True)
    wap_end_time = models.IntegerField(blank=True, null=True)
    web_start_time = models.IntegerField(blank=True, null=True)
    web_end_time = models.IntegerField(blank=True, null=True)
    app_sort = models.IntegerField(blank=True, null=True)
    wap_sort = models.IntegerField(blank=True, null=True)
    web_sort = models.IntegerField(blank=True, null=True)
    target_type = models.CharField(max_length=30, blank=True, null=True)
    target_info = models.CharField(max_length=255, blank=True, null=True)
    notice_text = models.TextField(blank=True, null=True)
    notice_type = models.IntegerField(blank=True, null=True)
    notice_again = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    page_code = models.CharField(max_length=30)
    is_visible_app = models.IntegerField(blank=True, null=True)
    is_visible_ouch_app = models.IntegerField(blank=True, null=True)
    is_visible_xcx = models.IntegerField(blank=True, null=True)
    is_visible_ouch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_advertisements_shop'


class CbdAdvertisementsTide(models.Model):
    name = models.CharField(max_length=100)
    media = models.CharField(max_length=200)
    position_id = models.IntegerField()
    target_type = models.IntegerField()
    target = models.CharField(max_length=200)
    gender = models.IntegerField()
    ad_key = models.CharField(max_length=200)
    sort = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    status = models.IntegerField()
    is_delete = models.IntegerField()
    page_code = models.CharField(max_length=30)
    type = models.IntegerField(blank=True, null=True)
    is_visible_app = models.IntegerField(blank=True, null=True)
    is_visible_ouch_app = models.IntegerField(blank=True, null=True)
    is_visible_dress_app = models.IntegerField(blank=True, null=True)
    is_visible_xcx = models.IntegerField(blank=True, null=True)
    is_visible_ouch = models.IntegerField(blank=True, null=True)
    is_visible_dress = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_advertisements_tide'


class CbdAgent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    agent_name = models.CharField(max_length=150, blank=True, null=True)
    cooperative_time_start = models.IntegerField(blank=True, null=True)
    cooperative_time_end = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_agent'


class CbdAlipayLog(models.Model):
    out_trade_no = models.CharField(max_length=64, blank=True, null=True)
    trade_no = models.CharField(max_length=64, blank=True, null=True)
    trade_status = models.CharField(max_length=64, blank=True, null=True)
    seller_id = models.CharField(max_length=30, blank=True, null=True)
    seller_email = models.CharField(max_length=100, blank=True, null=True)
    buyer_id = models.CharField(max_length=30, blank=True, null=True)
    buyer_email = models.CharField(max_length=100, blank=True, null=True)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)
    gmt_payment = models.DateTimeField(blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notify_time = models.DateTimeField(blank=True, null=True)
    notify_type = models.CharField(max_length=64, blank=True, null=True)
    notify_id = models.CharField(max_length=64, blank=True, null=True)
    os = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_alipay_log'


class CbdAmountUndertaker(models.Model):
    undertaker_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    supplier_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cbd_amount_undertaker'


class CbdAnchor(models.Model):
    anchor_id = models.AutoField(primary_key=True)
    activity_model_id = models.IntegerField()
    anchor_name = models.CharField(max_length=255)
    anchor_top_img = models.CharField(max_length=255, blank=True, null=True)
    show_goods = models.IntegerField(blank=True, null=True)
    goods = models.TextField(blank=True, null=True)
    show_special = models.IntegerField(blank=True, null=True)
    special = models.TextField(blank=True, null=True)
    anchor_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_anchor'


class CbdAnchorImg(models.Model):
    anchor_img_id = models.AutoField(primary_key=True)
    anchor_id = models.IntegerField()
    img_url = models.CharField(max_length=200, blank=True, null=True)
    img_target_type = models.IntegerField(blank=True, null=True)
    img_target = models.IntegerField(blank=True, null=True)
    img_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_anchor_img'


class CbdAnnouncementActivityLog(models.Model):
    queue = models.CharField(max_length=50)
    batch_no = models.CharField(max_length=50)
    sync_data = models.CharField(max_length=1000, blank=True, null=True)
    error_message = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField()
    mail_status = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_announcement_activity_log'


class CbdAnnualUser(models.Model):
    user_id = models.BigIntegerField()
    nickname = models.CharField(max_length=100)
    avatar = models.CharField(max_length=200)
    goods_id = models.IntegerField()
    goods_img = models.CharField(max_length=150)
    goods_name = models.CharField(max_length=200)
    spec_id = models.IntegerField()
    share_blessing = models.CharField(max_length=200)
    max_num = models.PositiveIntegerField()
    current_num = models.PositiveIntegerField()
    share_num = models.IntegerField()
    create_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_annual_user'


class CbdAnnualUserGroup(models.Model):
    annual_id = models.PositiveIntegerField()
    user_id = models.BigIntegerField()
    identity = models.PositiveIntegerField()
    nickname = models.CharField(max_length=200)
    avatar = models.CharField(max_length=200)
    create_time = models.PositiveIntegerField()
    is_hit = models.PositiveIntegerField()
    hit_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_annual_user_group'


class CbdApilog(models.Model):
    log_id = models.AutoField(primary_key=True)
    operate = models.CharField(max_length=20, blank=True, null=True)
    behavior = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    operator = models.CharField(max_length=20, blank=True, null=True)
    logtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_apilog'
        unique_together = (('log_id', 'logtime'),)


class CbdAppClassifyTemplate(models.Model):
    model_id = models.IntegerField()
    title = models.CharField(max_length=120)
    sort = models.IntegerField()
    create_time = models.IntegerField()
    create_user = models.CharField(max_length=100)
    update_time = models.IntegerField()
    update_user = models.CharField(max_length=100)
    user_type = models.IntegerField()
    app_type = models.IntegerField()
    is_kill = models.IntegerField()
    is_show = models.IntegerField()
    show_time = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    page_code = models.CharField(max_length=30)
    suit_sj_app = models.IntegerField()
    suit_tm_app = models.IntegerField()
    suit_sj_small = models.IntegerField()
    suit_yx_app = models.IntegerField()
    suit_db_app = models.IntegerField()
    activity_tag = models.CharField(max_length=30)
    suit_yx_small = models.IntegerField()
    suit_db_small = models.IntegerField()
    version_start = models.CharField(max_length=20)
    version_end = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cbd_app_classify_template'


class CbdAppTemplate(models.Model):
    model_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    app_type = models.IntegerField(blank=True, null=True)
    is_kill = models.IntegerField(blank=True, null=True)
    is_show = models.IntegerField(blank=True, null=True)
    show_time = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    page_code = models.CharField(max_length=30, blank=True, null=True)
    suit_sj_app = models.IntegerField(blank=True, null=True)
    suit_tm_app = models.IntegerField(blank=True, null=True)
    suit_sj_small = models.IntegerField(blank=True, null=True)
    suit_yx_app = models.IntegerField(blank=True, null=True)
    suit_db_app = models.IntegerField(blank=True, null=True)
    activity_tag = models.CharField(max_length=30, blank=True, null=True)
    suit_yx_small = models.IntegerField(blank=True, null=True)
    suit_db_small = models.IntegerField(blank=True, null=True)
    version_start = models.CharField(max_length=20, blank=True, null=True)
    version_end = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_app_template'


class CbdAppTemplateShop(models.Model):
    model_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    app_type = models.IntegerField(blank=True, null=True)
    is_show = models.IntegerField()
    gender = models.IntegerField(blank=True, null=True)
    page_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_app_template_shop'


class CbdAppTemplateTide(models.Model):
    model_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=120, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)
    app_type = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    page_code = models.CharField(max_length=30, blank=True, null=True)
    is_visible_app = models.IntegerField(blank=True, null=True)
    is_visible_ouch_app = models.IntegerField(blank=True, null=True)
    is_visible_dress_app = models.IntegerField(blank=True, null=True)
    is_visible_xcx = models.IntegerField(blank=True, null=True)
    is_visible_ouch = models.IntegerField(blank=True, null=True)
    is_visible_dress = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_app_template_tide'


class CbdAssistanceFree(models.Model):
    assistance_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(unique=True, blank=True, null=True)
    assistance_num = models.IntegerField(blank=True, null=True)
    virtual_assistance_num = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_assistance_free'


class CbdBargainActivities(models.Model):
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    bargain_type = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bargain_activities'


class CbdBargainActivitiesGoods(models.Model):
    bargain_activities_id = models.IntegerField()
    goods_id = models.IntegerField(blank=True, null=True)
    special_id = models.IntegerField(blank=True, null=True)
    goods_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bargain_activities_goods'


class CbdBargainBankBak(models.Model):
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    bear_side = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bargain_bank_bak'


class CbdBargainDetail(models.Model):
    bargain_id = models.IntegerField()
    user_id = models.BigIntegerField()
    add_time = models.IntegerField()
    os = models.CharField(max_length=10)
    initiator = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    finishamount = models.DecimalField(db_column='finishAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bargain_detail'


class CbdBargainGoods(models.Model):
    goods_id = models.IntegerField(blank=True, null=True)
    goods_name = models.CharField(max_length=30, blank=True, null=True)
    sort_man = models.IntegerField(blank=True, null=True)
    sort_woman = models.IntegerField(blank=True, null=True)
    bear_side = models.IntegerField(blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bargain_goods'


class CbdBargainGoodsBak(models.Model):
    bank_id = models.IntegerField()
    goods_id = models.IntegerField()
    cut_num = models.IntegerField(blank=True, null=True)
    cut_sale = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    bear_side = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bargain_goods_bak'


class CbdBargainGoodsCount(models.Model):
    count_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(unique=True)
    virtual_bargain_num = models.IntegerField(blank=True, null=True)
    bargain_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bargain_goods_count'


class CbdBargainMain(models.Model):
    bargain_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    address_id = models.IntegerField()
    spec_id = models.IntegerField(blank=True, null=True)
    add_time = models.IntegerField()
    expire_time = models.IntegerField()
    os = models.CharField(max_length=10)
    state = models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_no = models.BigIntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bargain_main'


class CbdBargainOpenAccount(models.Model):
    type = models.IntegerField()
    openid = models.CharField(max_length=60)
    nickname = models.CharField(max_length=50)
    head_portrait_url = models.TextField()
    add_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()
    app_source = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bargain_open_account'
        unique_together = (('type', 'openid'),)


class CbdBaskAttr(models.Model):
    attr_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    tag_id = models.IntegerField()
    user_id = models.BigIntegerField()
    bo_id = models.IntegerField()
    spec_id = models.IntegerField(blank=True, null=True)
    tag_belong = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bask_attr'


class CbdBaskLike(models.Model):
    bl_id = models.AutoField(primary_key=True)
    bo_id = models.IntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)
    click_time = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bask_like'


class CbdBaskOrder(models.Model):
    bo_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    goods_pic = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    bask_time = models.IntegerField(blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    spec_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=60, blank=True, null=True)
    skusize = models.CharField(max_length=60, blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)
    score = models.PositiveIntegerField()
    is_process = models.IntegerField(blank=True, null=True)
    processor = models.CharField(max_length=100, blank=True, null=True)
    pass_user = models.CharField(max_length=50, blank=True, null=True)
    operate_time = models.IntegerField(blank=True, null=True)
    order_detail_no = models.CharField(max_length=40, blank=True, null=True)
    bask_type = models.IntegerField(blank=True, null=True)
    is_hot = models.IntegerField(blank=True, null=True)
    rand_like = models.IntegerField(blank=True, null=True)
    is_pic = models.IntegerField()
    score_desc = models.IntegerField()
    score_logistics = models.IntegerField()
    score_service = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_bask_order'


class CbdBaskOrderOperationLog(models.Model):
    bask_order_id = models.IntegerField()
    create_time = models.IntegerField()
    operator = models.CharField(max_length=100)
    content = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_bask_order_operation_log'


class CbdBaskPic(models.Model):
    pic_id = models.AutoField(primary_key=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    thumb81 = models.CharField(max_length=200, blank=True, null=True)
    bo_id = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    thumb110 = models.CharField(max_length=200, blank=True, null=True)
    thumb123 = models.CharField(max_length=200, blank=True, null=True)
    thumb183 = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bask_pic'


class CbdBigBandnow(models.Model):
    id = models.IntegerField(primary_key=True)
    spec_ids = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_big_bandnow'


class CbdBindApp(models.Model):
    special_id = models.IntegerField(blank=True, null=True)
    app_url = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_bind_app'


class CbdBlackUsers(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    reason = models.CharField(max_length=100)
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_black_users'


class CbdBoost(models.Model):
    order_id = models.BigIntegerField()
    order_no = models.CharField(max_length=40)
    user_id = models.BigIntegerField()
    nickname = models.CharField(max_length=50)
    avatar = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    share_num = models.IntegerField()
    status = models.PositiveIntegerField()
    withdraw_notice = models.IntegerField()
    aboutto_end_notice = models.IntegerField()
    handle_status_time = models.IntegerField()
    is_timeout = models.IntegerField()
    is_reg_create = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_boost'


class CbdBoostBalance(models.Model):
    user_id = models.BigIntegerField(unique=True)
    undrawn_balance = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2)
    can_withdraw_balance = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.PositiveIntegerField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_boost_balance'


class CbdBoostBalanceChangeLog(models.Model):
    user_id = models.BigIntegerField()
    boost_id = models.IntegerField()
    src_user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    reason = models.PositiveIntegerField()
    undrawn_balance_before = models.DecimalField(max_digits=10, decimal_places=2)
    undrawn_balance_change = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance_before = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance_change = models.DecimalField(max_digits=10, decimal_places=2)
    can_withdraw_balance_before = models.DecimalField(max_digits=10, decimal_places=2)
    can_withdraw_balance_change = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_boost_balance_change_log'


class CbdBoostCollect(models.Model):
    data_date = models.DateField(unique=True, blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    share_order_num = models.IntegerField(blank=True, null=True)
    order_share_rate = models.FloatField(blank=True, null=True)
    total_payamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_share_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_share_user_num = models.IntegerField(blank=True, null=True)
    avg_share_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    boost_success_order_num = models.IntegerField(blank=True, null=True)
    total_boost_num = models.IntegerField(blank=True, null=True)
    new_user_boost_num = models.IntegerField(blank=True, null=True)
    old_user_boost_num = models.IntegerField(blank=True, null=True)
    boost_success_avg_num = models.FloatField(blank=True, null=True)
    new_boost_user_order_num = models.IntegerField(blank=True, null=True)
    boost_uv = models.IntegerField(blank=True, null=True)
    boost_new_reg = models.IntegerField(blank=True, null=True)
    today_boost_new_reg_user_num = models.IntegerField(blank=True, null=True)
    boost_new_pay_kedan = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    boost_new_pay_per = models.FloatField(blank=True, null=True)
    totay_boost_pay_per = models.FloatField(blank=True, null=True)
    avg_boost_num = models.FloatField(blank=True, null=True)
    boost_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    avg_boost_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    b_boost_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    withdrawal_ratio = models.FloatField(blank=True, null=True)
    platform_total_money = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    day_consumer_money = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    already_withdrawal_total_money = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    user_ava_already_withdrawal_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    join_boost_old_user_num = models.IntegerField(blank=True, null=True)
    join_boost_user_no_pay_num = models.IntegerField(blank=True, null=True)
    share_order_total_num = models.IntegerField(blank=True, null=True)
    share_pv = models.IntegerField(blank=True, null=True)
    avg_share_pv = models.FloatField(blank=True, null=True)
    share_avg_boost_num = models.FloatField(blank=True, null=True)
    new_user_pay_convert_rate = models.FloatField(blank=True, null=True)
    reg_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    increase_order_share_rate = models.FloatField(blank=True, null=True)
    increase_share_avg_boost_num = models.FloatField(blank=True, null=True)
    increase_new_user_pay_convert_rate = models.FloatField(blank=True, null=True)
    new_customer_boost_money_deposit_user_num = models.IntegerField(blank=True, null=True)
    click_share_page_uv = models.IntegerField(blank=True, null=True)
    boost_new_reg_user_num = models.IntegerField(blank=True, null=True)
    new_customer_boost_deposit_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_boost_collect'


class CbdBoostLog(models.Model):
    user_id = models.BigIntegerField()
    s_user_id = models.BigIntegerField()
    content = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_boost_log'


class CbdBoostUser(models.Model):
    b_id = models.IntegerField()
    order_id = models.BigIntegerField()
    order_no = models.CharField(max_length=40)
    user_id = models.BigIntegerField()
    nickname = models.CharField(max_length=50)
    avatar = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    identity = models.PositiveIntegerField()
    get_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_use = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_boost_user'


class CbdBoostUserLog(models.Model):
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    boost_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    result = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_boost_user_log'


class CbdBoostUserReg(models.Model):
    user_id = models.BigIntegerField(unique=True)
    b_user_id = models.BigIntegerField()
    boost_id = models.IntegerField()
    user_score = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_boost_user_reg'


class CbdBoostUserStat(models.Model):
    user_id = models.BigIntegerField(unique=True)
    boost_times = models.IntegerField()
    boost_amount = models.DecimalField(max_digits=10, decimal_places=2)
    first_boost_id = models.IntegerField()
    first_boost_amount = models.DecimalField(max_digits=10, decimal_places=2)
    first_boost_time = models.IntegerField()
    last_boost_id = models.IntegerField()
    last_boost_amount = models.DecimalField(max_digits=10, decimal_places=2)
    last_boost_time = models.IntegerField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_boost_user_stat'


class CbdBrand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=100, blank=True, null=True)
    cate_id = models.PositiveIntegerField()
    tag = models.CharField(max_length=30)
    introduce = models.TextField(blank=True, null=True)
    img = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    final_editor = models.CharField(max_length=100, blank=True, null=True)
    final_edit_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    brand_view = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    fbs_brand_id = models.IntegerField()
    max_like = models.PositiveIntegerField()
    like_num = models.PositiveIntegerField()
    history_like_num = models.PositiveIntegerField()
    history_sale_amount = models.DecimalField(max_digits=10, decimal_places=2)
    enter_time = models.PositiveIntegerField()
    is_flash_down = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    brand_type = models.IntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    level = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField(blank=True, null=True)
    is_using = models.IntegerField()
    promoted_tweets = models.CharField(max_length=500)
    first_letter = models.CharField(max_length=1, blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    display_in_xcx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_brand'


class CbdBrandOperationProperty(models.Model):
    brand_id = models.IntegerField(unique=True)
    latest_month_sale = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_brand_operation_property'


class CbdBrandScreams(models.Model):
    good_ids = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_brand_screams'


class CbdBrandSize(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    disable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_brand_size'


class CbdBrandSize0301(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    disable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_brand_size0301'


class CbdBrandStyle(models.Model):
    relation_id = models.AutoField(primary_key=True)
    brand_id = models.IntegerField()
    style_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_brand_style'
        unique_together = (('brand_id', 'style_id'),)


class CbdBrandtrendbenefit(models.Model):
    bdd_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    is_delete = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    issue_channel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_brandtrendbenefit'


class CbdBrandtrendbenefitSub(models.Model):
    bs_id = models.AutoField(primary_key=True)
    bdd_id = models.PositiveIntegerField()
    target_id = models.PositiveIntegerField()
    is_delete = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_brandtrendbenefit_sub'


class CbdBuyFdcSend(models.Model):
    order_id = models.BigIntegerField()
    type = models.IntegerField()
    content = models.CharField(max_length=500)
    is_send = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_buy_fdc_send'


class CbdBuyOrderLog(models.Model):
    order_id = models.BigIntegerField()
    content = models.CharField(max_length=500)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_buy_order_log'


class CbdBuyUserReg(models.Model):
    user_id = models.BigIntegerField(unique=True)
    order_id = models.BigIntegerField()
    nick_name = models.CharField(max_length=20)
    b_user_id = models.BigIntegerField()
    b_nick_name = models.CharField(max_length=20)
    b_order_id = models.BigIntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_buy_user_reg'


class CbdBuyUserSend(models.Model):
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    order_id = models.BigIntegerField()
    order_no = models.CharField(max_length=40, blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    paytime = models.IntegerField()
    is_send = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_buy_user_send'


class CbdBuyUserSendCopy(models.Model):
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    order_id = models.BigIntegerField()
    order_no = models.CharField(max_length=40, blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    paytime = models.IntegerField()
    is_send = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_buy_user_send_copy'


class CbdCallRecord(models.Model):
    id = models.PositiveIntegerField()
    unique_id = models.CharField(max_length=29)
    hotline = models.PositiveIntegerField()
    number_trunk = models.PositiveIntegerField()
    customer_number = models.CharField(max_length=15)
    customer_number_type = models.PositiveIntegerField()
    customer_area_code = models.CharField(max_length=4)
    customer_province = models.CharField(max_length=9)
    customer_crm_id = models.CharField()
    customer_city = models.CharField(max_length=21)
    customer_vip = models.PositiveIntegerField()
    client_number = models.CharField(max_length=11)
    client_area_code = models.CharField(max_length=3)
    client_name = models.CharField(max_length=9)
    client_crm_id = models.CharField()
    cno = models.CharField(max_length=4)
    exten = models.CharField()
    start_time = models.PositiveIntegerField()
    answer_time = models.PositiveIntegerField()
    join_queue_time = models.PositiveIntegerField()
    bridge_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    bill_duration = models.PositiveSmallIntegerField()
    bridge_duration = models.PositiveSmallIntegerField()
    total_duration = models.PositiveSmallIntegerField()
    cost = models.DecimalField(max_digits=14, decimal_places=3)
    ivr_id = models.PositiveSmallIntegerField()
    ivr_name = models.CharField(max_length=21)
    ivr_flow = models.CharField(max_length=255)
    queue_name = models.CharField(max_length=11)
    record_file = models.CharField(max_length=91)
    score = models.PositiveIntegerField()
    score_comment = models.CharField()
    in_case_lib = models.PositiveIntegerField()
    call_type = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    mark = models.PositiveIntegerField()
    mark_data = models.CharField()
    end_reason = models.PositiveSmallIntegerField()
    gw_ip = models.CharField(max_length=11)
    processed = models.PositiveIntegerField()
    process_comment = models.CharField(blank=True, null=True)
    user_field = models.CharField()
    sip_cause = models.PositiveIntegerField()
    asr_duration = models.PositiveIntegerField()
    asr_cost = models.DecimalField(max_digits=6, decimal_places=3)
    create_time = models.DateTimeField()
    date_type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_call_record'


class CbdCancelOrderAfterPay(models.Model):
    order_id = models.BigIntegerField()
    remark = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_cancel_order_after_pay'


class CbdCanceledSoonOrder(models.Model):
    c_id = models.AutoField(primary_key=True)
    orders_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_canceled_soon_order'


class CbdCartGift(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    special_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    spec_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_cart_gift'


class CbdCartRecommendGoods(models.Model):
    goods_id = models.IntegerField()
    is_visible_sdj = models.IntegerField()
    is_visible_ouch = models.IntegerField()
    sort = models.SmallIntegerField()
    create_uid = models.IntegerField()
    create_name = models.CharField(max_length=255)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_cart_recommend_goods'


class CbdCashGiftGoods(models.Model):
    sort_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(unique=True, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_cash_gift_goods'


class CbdCatAppTagCache(models.Model):
    app_id = models.CharField(max_length=32)
    tags = models.TextField(blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_cat_app_tag_cache'


class CbdCatOperationProperty(models.Model):
    cat_id = models.IntegerField(unique=True)
    goods_num = models.PositiveIntegerField()
    latest_week_sale = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_cat_operation_property'


class CbdCateCount(models.Model):
    type = models.IntegerField(blank=True, null=True)
    click_num = models.IntegerField(blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_num = models.IntegerField(blank=True, null=True)
    user_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    version = models.CharField(max_length=15, blank=True, null=True)
    os = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_cate_count'


class CbdCateTag(models.Model):
    tt_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=100, blank=True, null=True)
    tp_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField()
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_cate_tag'


class CbdCategorySize(models.Model):
    size_id = models.AutoField(primary_key=True)
    cate_id = models.IntegerField()
    size_name = models.CharField(max_length=50)
    size = models.CharField(max_length=150)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_category_size'


class CbdCategoryTag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    cate_id = models.IntegerField()
    tag_name = models.CharField(max_length=50)
    tag_type = models.IntegerField(blank=True, null=True)
    click_num = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_category_tag'


class CbdChannel(models.Model):
    channel_id = models.IntegerField(blank=True, null=True)
    channel_no = models.CharField(unique=True, max_length=100, blank=True, null=True)
    channel_name = models.CharField(max_length=200, blank=True, null=True)
    channel_type = models.PositiveIntegerField()
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_channel'


class CbdChannelCurrentData(models.Model):
    app_type = models.IntegerField()
    data_date = models.DateField()
    active_spread_name = models.CharField(max_length=100)
    active_os = models.CharField(max_length=100)
    active_user_num = models.IntegerField(blank=True, null=True)
    active_reg_user_num = models.IntegerField(blank=True, null=True)
    active_first_login_non_platform_reg_user_num = models.IntegerField(blank=True, null=True)
    active_reg_new_user_num = models.IntegerField(blank=True, null=True)
    active_reg_new_user_order_num = models.IntegerField(blank=True, null=True)
    active_reg_new_user_per_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    active_reg_new_user_total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reg_user_num = models.IntegerField(blank=True, null=True)
    first_login_non_platform_reg_user_num = models.IntegerField(blank=True, null=True)
    new_user_total_user_num = models.IntegerField(blank=True, null=True)
    new_user_total_order_num = models.IntegerField(blank=True, null=True)
    new_user_total_per_amount = models.IntegerField(blank=True, null=True)
    new_user_total_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_user_num = models.IntegerField(blank=True, null=True)
    total_order_num = models.IntegerField(blank=True, null=True)
    total_per_amount = models.IntegerField(blank=True, null=True)
    total_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.DateTimeField()
    active_reg_pay_vip_user = models.IntegerField(blank=True, null=True)
    active_reg_pay_vip_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    active_reg_pay_vip_pre_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_channel_current_data'
        unique_together = (('app_type', 'data_date', 'active_spread_name', 'active_os'),)


class CbdChannelCurrentDataNew(models.Model):
    app_type = models.IntegerField()
    data_date = models.DateField()
    active_spread_name = models.CharField(max_length=100)
    active_os = models.CharField(max_length=100)
    active_user_num = models.IntegerField(blank=True, null=True)
    active_reg_user_num = models.IntegerField(blank=True, null=True)
    active_first_login_non_platform_reg_user_num = models.IntegerField(blank=True, null=True)
    active_reg_new_user_num = models.IntegerField(blank=True, null=True)
    active_reg_new_user_order_num = models.IntegerField(blank=True, null=True)
    active_reg_new_user_per_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    active_reg_new_user_total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reg_user_num = models.IntegerField(blank=True, null=True)
    first_login_non_platform_reg_user_num = models.IntegerField(blank=True, null=True)
    new_user_total_user_num = models.IntegerField(blank=True, null=True)
    new_user_total_order_num = models.IntegerField(blank=True, null=True)
    new_user_total_per_amount = models.IntegerField(blank=True, null=True)
    new_user_total_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_user_num = models.IntegerField(blank=True, null=True)
    total_order_num = models.IntegerField(blank=True, null=True)
    total_per_amount = models.IntegerField(blank=True, null=True)
    total_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.DateTimeField()
    active_reg_pay_vip_user = models.IntegerField(blank=True, null=True)
    active_reg_pay_vip_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    active_reg_pay_vip_pre_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_channel_current_data_new'
        unique_together = (('app_type', 'data_date', 'active_spread_name', 'active_os'),)


class CbdChannelTag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(unique=True, max_length=80)
    android_condition = models.CharField(max_length=80, blank=True, null=True)
    ios_condition = models.CharField(max_length=80, blank=True, null=True)
    activity_url = models.CharField(max_length=200, blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_channel_tag'


class CbdChinaRegion(models.Model):
    region_id = models.PositiveSmallIntegerField(primary_key=True)
    parent_id = models.PositiveSmallIntegerField()
    region_name = models.CharField(max_length=120)
    region_type = models.IntegerField()
    agency_id = models.PositiveSmallIntegerField()
    another_name = models.CharField(max_length=120, blank=True, null=True)
    sort = models.PositiveIntegerField(blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    area_code = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_china_region'


class CbdCollectGoods(models.Model):
    collect_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_collect_goods'


class CbdCollectShop(models.Model):
    collect_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    store_id = models.IntegerField(blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_collect_shop'
        unique_together = (('user_id', 'store_id'),)


class CbdCommend(models.Model):
    goods_id = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_commend'


class CbdComments(models.Model):
    parent_id = models.PositiveIntegerField()
    comment_type = models.IntegerField()
    order_id = models.BigIntegerField()
    detail_no = models.CharField(max_length=64)
    user_name = models.CharField(max_length=100)
    user_id = models.BigIntegerField()
    shop_id = models.IntegerField()
    quality = models.IntegerField()
    attitude = models.IntegerField()
    speed = models.IntegerField()
    content = models.CharField(max_length=200, blank=True, null=True)
    add_time = models.PositiveIntegerField()
    status = models.IntegerField()
    update_time = models.IntegerField()
    update_user = models.CharField(max_length=64)
    is_show = models.PositiveIntegerField()
    is_deleted = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_comments'


class CbdComplaint(models.Model):
    order_id = models.BigIntegerField()
    detail_no = models.CharField(max_length=35)
    user_id = models.BigIntegerField()
    content = models.CharField(max_length=1000)
    version = models.CharField(max_length=50)
    os = models.CharField(max_length=20)
    is_fbs = models.PositiveIntegerField()
    shop_id = models.PositiveIntegerField()
    type = models.CharField(max_length=25, blank=True, null=True)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_complaint'


class CbdComplaintImg(models.Model):
    complaint_id = models.IntegerField()
    img_url = models.CharField(max_length=200)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_complaint_img'


class CbdConfig(models.Model):
    config_key = models.CharField(max_length=40)
    config_value = models.CharField(max_length=200)
    remark = models.CharField(max_length=20)
    sys = models.IntegerField()
    status = models.IntegerField()
    create_id = models.IntegerField()
    create_name = models.CharField(max_length=10)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_config'
        unique_together = (('config_key', 'sys'),)


class CbdCoupon(models.Model):
    coupon_id = models.AutoField(primary_key=True)
    coupon_type = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    category_ids = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    generate_amount = models.IntegerField()
    send_method = models.IntegerField(blank=True, null=True)
    use_condition_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    use_condition_type = models.IntegerField(blank=True, null=True)
    is_accumulate = models.IntegerField(blank=True, null=True)
    is_overlying = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    create_time = models.IntegerField()
    refuse_reason = models.CharField(max_length=255, blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_coupon'


class CbdCouponCode(models.Model):
    code_id = models.AutoField(primary_key=True)
    coupon_id = models.IntegerField()
    code = models.CharField(max_length=16)
    phone_no = models.CharField(max_length=12, blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    order_payamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    order_discount_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_coupon_code'


class CbdCouponCodeLog(models.Model):
    code_id = models.IntegerField()
    coupon_id = models.IntegerField()
    content = models.TextField()
    create_time = models.IntegerField()
    operation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_coupon_code_log'


class CbdCouponSpecial(models.Model):
    coupon_id = models.IntegerField(blank=True, null=True)
    special_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_coupon_special'


class CbdCrazyShopInfo(models.Model):
    title = models.CharField(max_length=255)
    up_time = models.IntegerField()
    down_time = models.IntegerField()
    goods_content = models.TextField()
    spec_content = models.TextField()
    create_time = models.IntegerField()
    activity_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_crazy_shop_info'


class CbdCrazyWeekend(models.Model):
    nav_id = models.AutoField(primary_key=True)
    nav_name = models.CharField(max_length=100, blank=True, null=True)
    nav_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_crazy_weekend'


class CbdCrazyWeekendSub(models.Model):
    nav_id = models.IntegerField(blank=True, null=True)
    bind_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_crazy_weekend_sub'


class CbdCsfeedback(models.Model):
    cs_id = models.AutoField(primary_key=True)
    msg_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    feedback_content = models.TextField(blank=True, null=True)
    feedback_time = models.IntegerField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_csfeedback'


class CbdCurrentConvert(models.Model):
    data_date = models.DateField(blank=True, null=True)
    data_hour = models.IntegerField(blank=True, null=True)
    new_man_uv = models.IntegerField(blank=True, null=True)
    new_woman_uv = models.IntegerField(blank=True, null=True)
    old_man_uv = models.IntegerField(blank=True, null=True)
    old_woman_uv = models.IntegerField(blank=True, null=True)
    new_man_order_count = models.IntegerField(blank=True, null=True)
    new_woman_order_count = models.IntegerField(blank=True, null=True)
    old_man_order_count = models.IntegerField(blank=True, null=True)
    old_woman_order_count = models.IntegerField(blank=True, null=True)
    new_man_sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    new_woman_sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    old_man_sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    old_woman_sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    new_man_per_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    new_woman_per_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    old_man_per_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    old_woman_per_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    new_man_convert = models.FloatField(blank=True, null=True)
    new_woman_convert = models.FloatField(blank=True, null=True)
    old_man_convert = models.FloatField(blank=True, null=True)
    old_woman_convert = models.FloatField(blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_current_convert'


class CbdDataSafeLog(models.Model):
    safe_log_id = models.AutoField(primary_key=True)
    log_type = models.IntegerField()
    group_title = models.CharField(max_length=20)
    class_title = models.CharField(max_length=20)
    action_title = models.CharField(max_length=20)
    log_content = models.CharField(max_length=500)
    user_account = models.CharField(max_length=20)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_data_safe_log'


class CbdDetailRecommend(models.Model):
    goods_id = models.IntegerField()
    operator = models.CharField(max_length=30)
    operator_time = models.DateTimeField()
    is_visible_sj_app = models.IntegerField()
    is_visible_yx_app = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_detail_recommend'


class CbdDetailRecommendGoods(models.Model):
    parent_id = models.IntegerField()
    recommend_goods_id = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_detail_recommend_goods'


class CbdDiscountCateList(models.Model):
    cate_id = models.IntegerField()
    cate_sort = models.IntegerField()
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_discount_cate_list'


class CbdDiscountGoods(models.Model):
    cate_id = models.IntegerField()
    goods_name = models.CharField(max_length=200)
    goods_id = models.IntegerField()
    base = models.IntegerField()
    type = models.IntegerField()
    sort_man = models.IntegerField(blank=True, null=True)
    sort_woman = models.IntegerField(blank=True, null=True)
    add_base = models.IntegerField()
    app_price = models.DecimalField(max_digits=10, decimal_places=2)
    xcx_price = models.DecimalField(max_digits=10, decimal_places=2)
    mark = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_discount_goods'


class CbdDituiAccessToken(models.Model):
    reference_id = models.IntegerField()
    dev_id = models.CharField(max_length=60)
    os = models.CharField(max_length=10, blank=True, null=True)
    token = models.CharField(max_length=16)
    app_resource = models.IntegerField()
    last_update = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_ditui_access_token'
        unique_together = (('reference_id', 'dev_id', 'app_resource'),)


class CbdDouble1Speeddating(models.Model):
    user_id = models.BigIntegerField()
    man_name = models.CharField(max_length=50)
    woman_name = models.CharField(max_length=50)
    add_time = models.IntegerField()
    result = models.CharField(max_length=50)
    score = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_double1_speeddating'


class CbdEarnAccount(models.Model):
    user_id = models.BigIntegerField(unique=True)
    nickname = models.CharField(max_length=100)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    init_balance = models.DecimalField(max_digits=10, decimal_places=2)
    total_commission = models.DecimalField(max_digits=10, decimal_places=2)
    last_month_expect_commission = models.DecimalField(max_digits=10, decimal_places=2)
    last_month_actual_commission = models.DecimalField(max_digits=10, decimal_places=2)
    invite_num = models.PositiveIntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    is_send = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_earn_account'


class CbdEarnAccountT(models.Model):
    user_id = models.BigIntegerField(unique=True)
    nickname = models.CharField(max_length=100)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    init_balance = models.DecimalField(max_digits=10, decimal_places=2)
    total_commission = models.DecimalField(max_digits=10, decimal_places=2)
    last_month_expect_commission = models.DecimalField(max_digits=10, decimal_places=2)
    last_month_actual_commission = models.DecimalField(max_digits=10, decimal_places=2)
    invite_num = models.PositiveIntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    is_send = models.IntegerField()
    secretary_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_earn_account_t'


class CbdEarnExpireLog(models.Model):
    user_id = models.BigIntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_earn_expire_log'


class CbdEarnOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    e_user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    detail_no = models.CharField(max_length=60)
    supplier_id = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    goods_img = models.CharField(max_length=200, blank=True, null=True)
    spec_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expect_commission = models.DecimalField(max_digits=10, decimal_places=2)
    actual_commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.PositiveIntegerField()
    create_time = models.IntegerField()
    complete_time = models.IntegerField(blank=True, null=True)
    is_legal = models.IntegerField()
    times = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_earn_order'


class CbdEarnOrderLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    content = models.TextField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_earn_order_log'


class CbdEarnOrderT(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    e_user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    detail_no = models.CharField(max_length=60)
    supplier_id = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField()
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    goods_img = models.CharField(max_length=200, blank=True, null=True)
    spec_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expect_commission = models.DecimalField(max_digits=10, decimal_places=2)
    actual_commission = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.PositiveIntegerField()
    create_time = models.IntegerField()
    complete_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_earn_order_t'


class CbdEarnSecretary(models.Model):
    user_id = models.BigIntegerField()
    secretary_id = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_earn_secretary'


class CbdEarnStat(models.Model):
    date = models.DateField()
    user_id = models.BigIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_delete = models.PositiveIntegerField()
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_earn_stat'


class CbdEarnUserReg(models.Model):
    user_id = models.BigIntegerField(unique=True)
    avatar = models.CharField(max_length=255)
    nickname = models.CharField(max_length=100)
    e_user_id = models.BigIntegerField()
    create_time = models.IntegerField()
    last_order_id = models.BigIntegerField()
    last_order_time = models.IntegerField()
    last_order_commission = models.DecimalField(max_digits=10, decimal_places=2)
    order_num = models.PositiveIntegerField()
    last_order_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cbd_earn_user_reg'


class CbdEarnUserRegT(models.Model):
    user_id = models.BigIntegerField(unique=True)
    avatar = models.CharField(max_length=255)
    nickname = models.CharField(max_length=100)
    e_user_id = models.BigIntegerField()
    create_time = models.IntegerField()
    last_order_id = models.BigIntegerField()
    last_order_time = models.IntegerField()
    last_order_commission = models.DecimalField(max_digits=10, decimal_places=2)
    order_num = models.PositiveIntegerField()
    last_order_amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cbd_earn_user_reg_t'


class CbdEarnUserSecretary(models.Model):
    secretary_id = models.AutoField(primary_key=True)
    avatar = models.CharField(max_length=255)
    nickname = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_earn_user_secretary'


class CbdEarningCategory(models.Model):
    cate_id = models.IntegerField()
    pid = models.PositiveIntegerField(blank=True, null=True)
    tpl = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200)
    type = models.CharField(max_length=60, blank=True, null=True)
    banner = models.CharField(max_length=64)
    name = models.CharField(max_length=120, blank=True, null=True)
    channel = models.CharField(max_length=30)
    sort = models.IntegerField()
    display = models.CharField(max_length=10, blank=True, null=True)
    status = models.PositiveIntegerField()
    is_display = models.IntegerField()
    level = models.PositiveIntegerField()
    icons = models.CharField(max_length=200)
    icons0 = models.CharField(max_length=200, blank=True, null=True)
    icons1 = models.CharField(max_length=200, blank=True, null=True)
    icons2 = models.CharField(max_length=200, blank=True, null=True)
    icons3 = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    nav = models.CharField(max_length=10, blank=True, null=True)
    count = models.CharField(max_length=20)
    keyword = models.CharField(max_length=255)
    description = models.TextField()
    lang = models.CharField(max_length=10, blank=True, null=True)
    cate_img = models.CharField(max_length=200, blank=True, null=True)
    cate_title = models.CharField(max_length=100, blank=True, null=True)
    font_color = models.CharField(max_length=10, blank=True, null=True)
    img_width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img_height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cate_img_1_61 = models.CharField(max_length=200, blank=True, null=True)
    cate_tab = models.CharField(max_length=200, blank=True, null=True)
    cate_tabclick = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=3, blank=True, null=True)
    cate_detail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'cbd_earning_category'


class CbdExpressCompany(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    status = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_express_company'


class CbdFaild(models.Model):
    faild_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    create_time = models.IntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_faild'


class CbdFbsMkfGoods(models.Model):
    batchno = models.IntegerField(db_column='batchNo', blank=True, null=True)  # Field name made lowercase.
    jmcode = models.CharField(db_column='jmCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supplierskucode = models.CharField(db_column='supplierSkuCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    barcode = models.CharField(db_column='barCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    brandcode = models.CharField(db_column='brandCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    jmskucode = models.CharField(db_column='jmskuCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extentioncode = models.CharField(db_column='extentionCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keyproperties = models.CharField(db_column='keyProperties', max_length=255, blank=True, null=True)  # Field name made lowercase.
    omsshopid = models.IntegerField(db_column='omsShopId', blank=True, null=True)  # Field name made lowercase.
    brandname = models.CharField(db_column='brandName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(max_length=20, blank=True, null=True)
    skusize = models.CharField(db_column='skuSize', max_length=20, blank=True, null=True)  # Field name made lowercase.
    goodssex = models.CharField(db_column='goodsSex', max_length=20, blank=True, null=True)  # Field name made lowercase.
    goodscrazyprice = models.DecimalField(db_column='goodsCrazyPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    goodsbarprice = models.DecimalField(db_column='goodsBarPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    goodsparams = models.TextField(db_column='goodsParams', blank=True, null=True)  # Field name made lowercase.
    goodscategorylevel1 = models.PositiveIntegerField(db_column='goodsCategoryLevel1', blank=True, null=True)  # Field name made lowercase.
    goodscategorylevel2 = models.PositiveIntegerField(db_column='goodsCategoryLevel2', blank=True, null=True)  # Field name made lowercase.
    goodscategorylevel3 = models.PositiveIntegerField(db_column='goodsCategoryLevel3', blank=True, null=True)  # Field name made lowercase.
    goodsbuyerid = models.PositiveIntegerField(db_column='goodsBuyerId', blank=True, null=True)  # Field name made lowercase.
    goodsskuup = models.PositiveIntegerField(db_column='goodsSkuUp', blank=True, null=True)  # Field name made lowercase.
    goodspageup = models.PositiveIntegerField(db_column='goodsPageUp', blank=True, null=True)  # Field name made lowercase.
    innergoodsstatus = models.PositiveIntegerField(db_column='innerGoodsStatus', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_fbs_mkf_goods'


class CbdFbsMkfGoodsStock(models.Model):
    batchno = models.PositiveIntegerField(db_column='batchNo', blank=True, null=True)  # Field name made lowercase.
    jmskucode = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    productcode = models.CharField(db_column='productCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extentioncode = models.CharField(db_column='extentionCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supplierskucode = models.CharField(db_column='supplierSkuCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keyproperties = models.CharField(db_column='keyProperties', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(blank=True, null=True)
    direction = models.IntegerField(blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    optime = models.DateTimeField(db_column='opTime', blank=True, null=True)  # Field name made lowercase.
    shopid = models.IntegerField(db_column='shopId', blank=True, null=True)  # Field name made lowercase.
    createtime = models.IntegerField(db_column='createTime', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(blank=True, null=True)
    task_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_fbs_mkf_goods_stock'


class CbdFbsMkfTask(models.Model):
    queue = models.CharField(max_length=50)
    batch_no = models.CharField(unique=True, max_length=100)
    task_data = models.TextField(blank=True, null=True)
    add_time = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    msg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_fbs_mkf_task'


class CbdFbsMkfTaskArchive2016(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    queue = models.CharField(max_length=50)
    batch_no = models.CharField(max_length=100)
    task_data = models.TextField(blank=True, null=True)
    add_time = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    msg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_fbs_mkf_task_archive_2016'


class CbdFbsMkfTaskArchive2017(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    queue = models.CharField(max_length=50)
    batch_no = models.CharField(max_length=100)
    task_data = models.TextField(blank=True, null=True)
    add_time = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    msg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_fbs_mkf_task_archive_2017'


class CbdFbsMkfTaskLog(models.Model):
    task_num = models.PositiveIntegerField()
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    duration = models.IntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_fbs_mkf_task_log'


class CbdFbsModuleAction(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    module_name = models.CharField(max_length=32)
    action_name = models.CharField(max_length=32)
    introduce = models.CharField(max_length=128)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_fbs_module_action'


class CbdFbsModuleActionCount(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    ma_id = models.PositiveSmallIntegerField()
    hits = models.PositiveIntegerField()
    click_time = models.IntegerField()
    create_time = models.IntegerField()
    module_name = models.CharField(max_length=32)
    action_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cbd_fbs_module_action_count'


class CbdFbsModuleActionDetail(models.Model):
    ma_id = models.PositiveSmallIntegerField()
    username = models.CharField(max_length=50)
    click_time = models.IntegerField()
    module_name = models.CharField(max_length=32)
    action_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cbd_fbs_module_action_detail'


class CbdFbsOfflineSpecialList(models.Model):
    off_id = models.AutoField(primary_key=True)
    batch_no = models.CharField(max_length=50)
    fbs_activity_id = models.TextField()
    action = models.IntegerField(blank=True, null=True)
    is_complete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_fbs_offline_special_list'


class CbdFbsTaoSameGoods(models.Model):
    fbs_id = models.PositiveIntegerField()
    pgoods_id = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    isdel = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_fbs_tao_same_goods'


class CbdFdcRefund(models.Model):
    refund_id = models.AutoField(primary_key=True)
    refund_no = models.CharField(unique=True, max_length=50)
    order_no = models.CharField(max_length=40)
    detail_no = models.CharField(max_length=50)
    goods_no = models.CharField(max_length=50)
    sku_no = models.CharField(max_length=100)
    refund_status = models.IntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_fdc_refund'


class CbdFeedback(models.Model):
    msg_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=60, blank=True, null=True)
    msg_title = models.CharField(max_length=200, blank=True, null=True)
    msg_content = models.TextField(blank=True, null=True)
    msg_time = models.IntegerField(blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    is_read = models.IntegerField(blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)
    opinion_type = models.PositiveIntegerField()
    order_ids = models.CharField(max_length=150, blank=True, null=True)
    goods_ids = models.CharField(max_length=150, blank=True, null=True)
    qq = models.CharField(max_length=15)
    mobile = models.CharField(max_length=20)
    operator = models.CharField(max_length=50, blank=True, null=True)
    operate_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_feedback'


class CbdFeedbackNote(models.Model):
    msg_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    action_desc = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_feedback_note'


class CbdFinance(models.Model):
    user_id = models.BigIntegerField()
    pay_type = models.PositiveIntegerField()
    app_resource = models.PositiveIntegerField()
    user_name = models.CharField(max_length=50)
    user_account = models.CharField(max_length=64)
    pay_money = models.DecimalField(max_digits=10, decimal_places=2)
    hand_fee = models.DecimalField(max_digits=7, decimal_places=2)
    create_time = models.PositiveIntegerField()
    act_user = models.CharField(max_length=20)
    act_time = models.PositiveIntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=39, blank=True, null=True)
    biz_no = models.CharField(max_length=64, blank=True, null=True)
    pay_date = models.CharField(max_length=20, blank=True, null=True)
    error_code = models.CharField(max_length=30)
    error_msg = models.CharField(max_length=255, blank=True, null=True)
    return_status = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    is_rollback = models.IntegerField()
    is_show = models.IntegerField()
    retry_times = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_finance'


class CbdFinanceLog(models.Model):
    finance_id = models.PositiveIntegerField()
    error_msg = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField()
    act_time = models.IntegerField()
    act_user = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_finance_log'


class CbdFlashFriends(models.Model):
    ff_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=100, blank=True, null=True)
    flash_friends_id = models.IntegerField(unique=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_active = models.SmallIntegerField(blank=True, null=True)
    ffriends_member = models.SmallIntegerField(blank=True, null=True)
    ff_user_name = models.CharField(max_length=100, blank=True, null=True)
    ff_discount = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    use_times = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_flash_friends'


class CbdFlashFriendsUseLog(models.Model):
    order_id = models.BigIntegerField(primary_key=True)
    flash_friends_id = models.PositiveIntegerField()
    is_return = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_flash_friends_use_log'


class CbdFlashSale(models.Model):
    flash_sale_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    coupon_id = models.CharField(max_length=50, blank=True, null=True)
    up_time = models.IntegerField(blank=True, null=True)
    down_time = models.IntegerField(blank=True, null=True)
    resource_state = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_flash_sale'


class CbdFlashSaleGoods(models.Model):
    goods_sort_id = models.AutoField(primary_key=True)
    flash_sale_id = models.IntegerField()
    goods_id = models.IntegerField()
    union_special_id = models.IntegerField(blank=True, null=True)
    min_crazy_price = models.DecimalField(max_digits=10, decimal_places=2)
    goods_sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_flash_sale_goods'


class CbdFlashSaleResource(models.Model):
    flash_sale_id = models.IntegerField()
    resource_img = models.CharField(max_length=200)
    target_type = models.IntegerField()
    target = models.CharField(max_length=200)
    sort = models.IntegerField()
    create_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_flash_sale_resource'


class CbdFlashSaleSpecial(models.Model):
    special_sort_id = models.AutoField(primary_key=True)
    flash_sale_id = models.IntegerField()
    brand_name = models.CharField(max_length=50, blank=True, null=True)
    goods_id = models.IntegerField()
    special_id = models.IntegerField()
    special_sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_flash_sale_special'


class CbdGameOrder(models.Model):
    g_id = models.PositiveIntegerField(primary_key=True)
    order_id = models.BigIntegerField()
    detail_no = models.CharField(max_length=60)
    game_id = models.IntegerField()
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    type = models.IntegerField()
    add_time = models.PositiveIntegerField()
    pay_state = models.IntegerField()
    is_send = models.IntegerField()
    is_first_order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_game_order'


class CbdGdtChannel(models.Model):
    source = models.CharField(unique=True, max_length=50)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    advertiser_id = models.CharField(max_length=20)
    encrypt_key = models.CharField(max_length=60)
    sign_key = models.CharField(max_length=60)
    os = models.CharField(max_length=7)
    user_action_code = models.PositiveSmallIntegerField()
    program_number = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_gdt_channel'


class CbdGetTelNumberLog(models.Model):
    ext_number = models.CharField(max_length=30, blank=True, null=True)
    customer_number = models.CharField(max_length=30, blank=True, null=True)
    tel_numbers = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    msg = models.CharField(max_length=100, blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_get_tel_number_log'


class CbdGoods(models.Model):
    goods_id = models.AutoField(primary_key=True)
    goods_bzno = models.CharField(unique=True, max_length=50, blank=True, null=True)
    cate = models.IntegerField(blank=True, null=True)
    second_cate = models.IntegerField(blank=True, null=True)
    three_cate = models.IntegerField(blank=True, null=True)
    brand_id = models.IntegerField()
    brand = models.CharField(max_length=100, blank=True, null=True)
    goods_type = models.IntegerField(blank=True, null=True)
    goods_brand = models.CharField(max_length=100, blank=True, null=True)
    goods_no = models.CharField(max_length=30, blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_html = models.TextField(blank=True, null=True)
    videourl = models.CharField(max_length=200, blank=True, null=True)
    coverurl = models.CharField(max_length=200, blank=True, null=True)
    base = models.IntegerField(blank=True, null=True)
    saletype = models.IntegerField(blank=True, null=True)
    open_time = models.IntegerField(blank=True, null=True)
    close_time = models.IntegerField(blank=True, null=True)
    activitycontent = models.TextField(blank=True, null=True)
    realnum = models.IntegerField(blank=True, null=True)
    viewnum = models.IntegerField(blank=True, null=True)
    surplus = models.IntegerField(blank=True, null=True)
    buyupnum = models.IntegerField(blank=True, null=True)
    label = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    is_top = models.IntegerField(blank=True, null=True)
    topnum = models.IntegerField(blank=True, null=True)
    tops_time = models.IntegerField(blank=True, null=True)
    tope_time = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    createtime = models.IntegerField(blank=True, null=True)
    freight_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    freight = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    brankcode = models.CharField(max_length=50, blank=True, null=True)
    goods_param = models.TextField(blank=True, null=True)
    skuorder = models.TextField(blank=True, null=True)
    praisenum = models.IntegerField(blank=True, null=True)
    breakage_text = models.CharField(max_length=255, blank=True, null=True)
    breakage_img = models.CharField(max_length=255, blank=True, null=True)
    special_id = models.IntegerField(blank=True, null=True)
    breakage_title = models.CharField(max_length=255, blank=True, null=True)
    buydownnum = models.IntegerField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    bathch = models.CharField(max_length=200, blank=True, null=True)
    salenum = models.IntegerField(blank=True, null=True)
    buyer = models.IntegerField(blank=True, null=True)
    spec_key = models.CharField(max_length=60, blank=True, null=True)
    batch_key = models.CharField(max_length=100, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    bak_buydownnum = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    consignment = models.IntegerField(blank=True, null=True)
    min_exp_date = models.CharField(max_length=10, blank=True, null=True)
    max_exp_date = models.CharField(max_length=10, blank=True, null=True)
    is_pack = models.IntegerField(blank=True, null=True)
    is_pack_goods = models.IntegerField(blank=True, null=True)
    brand_pic = models.CharField(max_length=100, blank=True, null=True)
    brand_content_pic = models.CharField(max_length=100, blank=True, null=True)
    brand_spec = models.CharField(max_length=100, blank=True, null=True)
    return_remark = models.TextField(blank=True, null=True)
    pack_goods = models.TextField(blank=True, null=True)
    cate_tag = models.IntegerField(blank=True, null=True)
    select_val = models.IntegerField(blank=True, null=True)
    goods_gif = models.CharField(max_length=200, blank=True, null=True)
    hdphoto = models.CharField(db_column='HDphoto', max_length=200, blank=True, null=True)  # Field name made lowercase.
    is_fbs = models.IntegerField(blank=True, null=True)
    fbs_version = models.CharField(max_length=10, blank=True, null=True)
    random_pack = models.IntegerField(blank=True, null=True)
    mis_buy_price = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    is_haitao = models.PositiveIntegerField()
    down_price = models.DecimalField(max_digits=10, decimal_places=0)
    goods_adjust_price_type = models.PositiveIntegerField()
    state = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    updatetime = models.PositiveIntegerField()
    saletime = models.IntegerField()
    checktime = models.IntegerField(blank=True, null=True)
    out_reason = models.CharField(max_length=200, blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    is_full_year_vendible = models.IntegerField()
    is_seckill = models.IntegerField()
    is_flash_down = models.IntegerField(blank=True, null=True)
    flash_down_num = models.IntegerField(blank=True, null=True)
    is_caveat_emptor = models.IntegerField(blank=True, null=True)
    is_copied = models.IntegerField()
    is_delete = models.IntegerField(blank=True, null=True)
    sdjj_cut = models.IntegerField(blank=True, null=True)
    for_spring = models.IntegerField(blank=True, null=True)
    for_summer = models.IntegerField(blank=True, null=True)
    for_autumn = models.IntegerField(blank=True, null=True)
    for_winter = models.IntegerField(blank=True, null=True)
    for_crowd = models.CharField(max_length=50, blank=True, null=True)
    cat_sort_score = models.IntegerField()
    taojj_state = models.IntegerField(blank=True, null=True)
    source_goods_id = models.IntegerField(blank=True, null=True)
    freight_tpl = models.IntegerField(blank=True, null=True)
    repeat_customers_sort = models.IntegerField(blank=True, null=True)
    new_customers_sort = models.IntegerField(blank=True, null=True)
    group_number = models.SmallIntegerField()
    hot_source = models.CharField(max_length=200)
    selling_point = models.CharField(max_length=200)
    per_month_buy_up = models.IntegerField(blank=True, null=True)
    is_hot_cake = models.IntegerField(blank=True, null=True)
    short_title = models.CharField(max_length=100, blank=True, null=True)
    limitation_times = models.IntegerField(blank=True, null=True)
    delivery_time_commitment = models.IntegerField(blank=True, null=True)
    is_return_change = models.IntegerField(blank=True, null=True)
    is_lost_ten = models.IntegerField(blank=True, null=True)
    max_reward = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    special_sale_status = models.IntegerField(blank=True, null=True)
    first_putaway_time = models.IntegerField(blank=True, null=True)
    merchant_subsidy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_showicon = models.PositiveIntegerField(blank=True, null=True)
    icon_show_start_time = models.PositiveIntegerField(blank=True, null=True)
    icon_show_end_time = models.PositiveIntegerField(blank=True, null=True)
    icon_good_detial = models.CharField(max_length=255, blank=True, null=True)
    icon_list = models.CharField(max_length=255, blank=True, null=True)
    icon_cart = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods'


class CbdGoodsAdditionalInfo(models.Model):
    goods_id = models.PositiveIntegerField(unique=True)
    stocknum = models.PositiveIntegerField()
    min_stocknum = models.PositiveIntegerField()
    max_stocknum = models.PositiveIntegerField()
    min_supply_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_supply_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_taojj_price = models.DecimalField(max_digits=10, decimal_places=2)
    max_taojj_price = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=30)
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_additional_info'


class CbdGoodsBoost(models.Model):
    user_id = models.BigIntegerField()
    order_no = models.CharField(max_length=30)
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    img_url = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField()
    boost_num = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address_id = models.IntegerField()
    create_time = models.IntegerField()
    end_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_boost'


class CbdGoodsBoostDetail(models.Model):
    boost_id = models.IntegerField()
    user_id = models.BigIntegerField()
    nickname = models.CharField(max_length=100, blank=True, null=True)
    account = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    create_time = models.IntegerField()
    is_read = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_boost_detail'


class CbdGoodsCategory(models.Model):
    pid = models.PositiveIntegerField(blank=True, null=True)
    tpl = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200)
    type = models.CharField(max_length=60, blank=True, null=True)
    banner = models.CharField(max_length=64)
    name = models.CharField(max_length=120, blank=True, null=True)
    channel = models.CharField(max_length=30)
    sort = models.IntegerField()
    display = models.CharField(max_length=10, blank=True, null=True)
    status = models.PositiveIntegerField()
    is_display = models.IntegerField()
    level = models.PositiveIntegerField()
    icons = models.CharField(max_length=200)
    icons0 = models.CharField(max_length=200, blank=True, null=True)
    icons1 = models.CharField(max_length=200, blank=True, null=True)
    icons2 = models.CharField(max_length=200, blank=True, null=True)
    icons3 = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    nav = models.CharField(max_length=10, blank=True, null=True)
    count = models.CharField(max_length=20)
    keyword = models.CharField(max_length=255)
    description = models.TextField()
    lang = models.CharField(max_length=10, blank=True, null=True)
    cate_img = models.CharField(max_length=200, blank=True, null=True)
    cate_title = models.CharField(max_length=100, blank=True, null=True)
    font_color = models.CharField(max_length=10, blank=True, null=True)
    img_width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    img_height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cate_img_1_61 = models.CharField(max_length=200, blank=True, null=True)
    cate_tab = models.CharField(max_length=200, blank=True, null=True)
    cate_tabclick = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=3, blank=True, null=True)
    cate_detail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'cbd_goods_category'


class CbdGoodsColorProposal(models.Model):
    goods_id = models.IntegerField()
    color = models.CharField(max_length=255)
    num = models.IntegerField()
    last_od_id = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_color_proposal'


class CbdGoodsConversion14D(models.Model):
    id = models.IntegerField(primary_key=True)
    data_date = models.DateField()
    goods_id = models.IntegerField()
    goods_conversion = models.DecimalField(max_digits=10, decimal_places=5)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_conversion_14d'
        unique_together = (('data_date', 'goods_id'),)


class CbdGoodsCurrentDay(models.Model):
    data_date = models.DateField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    man_uv = models.IntegerField(blank=True, null=True)
    man_pv = models.IntegerField(blank=True, null=True)
    woman_uv = models.IntegerField(blank=True, null=True)
    woman_pv = models.IntegerField(blank=True, null=True)
    man_order_num = models.IntegerField(blank=True, null=True)
    woman_order_num = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_current_day'
        unique_together = (('data_date', 'goods_id'),)


class CbdGoodsCurrentHour(models.Model):
    data_date = models.DateField(blank=True, null=True)
    data_hour = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    man_uv = models.IntegerField(blank=True, null=True)
    man_pv = models.IntegerField(blank=True, null=True)
    woman_uv = models.IntegerField(blank=True, null=True)
    woman_pv = models.IntegerField(blank=True, null=True)
    man_order_num = models.IntegerField(blank=True, null=True)
    woman_order_num = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_current_hour'
        unique_together = (('data_date', 'data_hour', 'goods_id'),)


class CbdGoodsCut(models.Model):
    cut_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    order_no = models.CharField(max_length=30)
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    goods_no = models.CharField(max_length=30)
    cut_num = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_subtract = models.DecimalField(max_digits=10, decimal_places=2)
    amount_left = models.DecimalField(max_digits=10, decimal_places=2)
    address_id = models.IntegerField()
    time_start = models.IntegerField()
    time_end = models.IntegerField()
    time_success = models.IntegerField()
    push_status = models.IntegerField()
    push_soon_success = models.IntegerField()
    push_fail_status = models.IntegerField()
    push_success = models.IntegerField()
    is_desc_stock = models.IntegerField()
    is_handle_stock = models.IntegerField()
    uuid = models.CharField(max_length=36)
    success_num = models.IntegerField()
    handle_num_time = models.IntegerField()
    handle_stock_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_cut'


class CbdGoodsCutAccess(models.Model):
    user_id = models.BigIntegerField(unique=True)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_cut_access'


class CbdGoodsCutDetail(models.Model):
    cut_detail_id = models.AutoField(primary_key=True)
    cut_id = models.IntegerField()
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    goods_no = models.CharField(max_length=30)
    amount_reduce = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_cut_detail'


class CbdGoodsCutUser(models.Model):
    user_id = models.BigIntegerField()
    num_order = models.IntegerField()
    num_able_cancel = models.IntegerField()
    num_able_cut = models.IntegerField()
    num_cut = models.IntegerField()
    update_time = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_cut_user'


class CbdGoodsCutUserLog(models.Model):
    user_id = models.BigIntegerField()
    order_no = models.CharField(max_length=50)
    history_data = models.CharField(max_length=250)
    current_data = models.CharField(max_length=250)
    operator = models.IntegerField()
    result = models.CharField(max_length=200)
    create_time = models.IntegerField()
    request_data = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'cbd_goods_cut_user_log'


class CbdGoodsDetailNotice(models.Model):
    notice_img = models.CharField(max_length=500, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_detail_notice'


class CbdGoodsDumpLog(models.Model):
    time = models.PositiveIntegerField()
    msg = models.TextField(blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_dump_log'


class CbdGoodsExt(models.Model):
    goods_id = models.PositiveIntegerField(unique=True)
    for_age = models.CharField(max_length=50)
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_ext'


class CbdGoodsHistoryData(models.Model):
    data_date = models.DateField()
    goods_id = models.IntegerField()
    click_num = models.IntegerField(blank=True, null=True)
    uv = models.IntegerField(blank=True, null=True)
    user_pv = models.IntegerField(blank=True, null=True)
    user_uv = models.IntegerField(blank=True, null=True)
    new_woman_pv = models.IntegerField(blank=True, null=True)
    new_woman_uv = models.IntegerField(blank=True, null=True)
    old_woman_pv = models.IntegerField(blank=True, null=True)
    old_woman_uv = models.IntegerField(blank=True, null=True)
    new_man_pv = models.IntegerField(blank=True, null=True)
    new_man_uv = models.IntegerField(blank=True, null=True)
    old_man_pv = models.IntegerField(blank=True, null=True)
    old_man_uv = models.IntegerField(blank=True, null=True)
    new_man_order_num = models.IntegerField(blank=True, null=True)
    new_woman_order_num = models.IntegerField(blank=True, null=True)
    old_man_order_num = models.IntegerField(blank=True, null=True)
    old_woman_order_num = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    order_num = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_history_data'
        unique_together = (('data_date', 'goods_id'),)


class CbdGoodsHistorySaleTop(models.Model):
    goods_id = models.IntegerField(blank=True, null=True)
    order_num = models.IntegerField(blank=True, null=True)
    payamount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    item_num = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_history_sale_top'


class CbdGoodsIcon(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    new_show_type = models.PositiveIntegerField()
    new_is_showicon = models.PositiveIntegerField(blank=True, null=True)
    new_icon_show_start_time = models.PositiveIntegerField(blank=True, null=True)
    new_icon_show_end_time = models.PositiveIntegerField(blank=True, null=True)
    new_icon_goods_detail = models.CharField(max_length=255, blank=True, null=True)
    new_icon_goods_t = models.CharField(max_length=255, blank=True, null=True)
    new_icon_list = models.CharField(max_length=255, blank=True, null=True)
    new_icon_cart = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_icon'


class CbdGoodsIconExt(models.Model):
    goods_id = models.PositiveIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_icon_ext'


class CbdGoodsKeywords(models.Model):
    keywords_name = models.CharField(max_length=50)
    sort = models.IntegerField()
    is_goods_sorted = models.IntegerField()
    is_delete = models.IntegerField()
    last_create_uid = models.IntegerField()
    last_create_name = models.CharField(max_length=64)
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_keywords'


class CbdGoodsKeywordsDetail(models.Model):
    goods_keywords_id = models.IntegerField()
    goods_id = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_keywords_detail'


class CbdGoodsKeywordsWords(models.Model):
    goods_keywords_id = models.IntegerField()
    words = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cbd_goods_keywords_words'


class CbdGoodsListSort(models.Model):
    sort_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    repeat_customers_sort = models.IntegerField(blank=True, null=True)
    female_repeat_customers_sort = models.IntegerField(blank=True, null=True)
    new_customers_sort = models.IntegerField(blank=True, null=True)
    female_new_customers_sort = models.IntegerField(blank=True, null=True)
    thirty_days_man_sort = models.IntegerField()
    thirty_days_woman_sort = models.IntegerField()
    sort_time = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_list_sort'
        unique_together = (('goods_id', 'category'),)


class CbdGoodsListSortBank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    category = models.IntegerField(blank=True, null=True)
    sort_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_list_sort_bank'
        unique_together = (('bank_id', 'goods_id'), ('goods_id', 'category', 'sort_type'),)


class CbdGoodsOperationProperty(models.Model):
    goods_id = models.IntegerField(unique=True)
    latest_week_sale = models.PositiveIntegerField()
    latest_month_sale = models.PositiveIntegerField()
    latest_week_click_div_sale = models.PositiveIntegerField()
    latest_week_goods_clicks = models.IntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_operation_property'


class CbdGoodsOutLog(models.Model):
    shop_id = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    status = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_out_log'


class CbdGoodsPropaganda(models.Model):
    propaganda_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    image = models.CharField(max_length=400)
    price_desc = models.CharField(max_length=10)
    price_color = models.CharField(max_length=10)
    benefit_point_color = models.CharField(max_length=10)
    activity_type = models.IntegerField()
    special_ids = models.TextField()
    goods_ids = models.TextField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_propaganda'


class CbdGoodsPropagandaSpecial(models.Model):
    special_id = models.IntegerField()
    propaganda_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_propaganda_special'


class CbdGoodsRelayReward(models.Model):
    goods_id = models.IntegerField(unique=True, blank=True, null=True)
    max_reward = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_relay_reward'


class CbdGoodsScene(models.Model):
    union_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    brand_id = models.IntegerField(blank=True, null=True)
    scene_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_scene'


class CbdGoodsSetTag(models.Model):
    content = models.TextField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    open_time = models.IntegerField(blank=True, null=True)
    close_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_set_tag'


class CbdGoodsSort(models.Model):
    sort_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    repeat_customers_sort = models.IntegerField(blank=True, null=True)
    female_repeat_customers_sort = models.IntegerField(blank=True, null=True)
    new_customers_sort = models.IntegerField(blank=True, null=True)
    female_new_customers_sort = models.IntegerField(blank=True, null=True)
    sort_time = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_sort'
        unique_together = (('goods_id', 'category'),)


class CbdGoodsSortBackups(models.Model):
    sort_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    repeat_customers_sort = models.IntegerField(blank=True, null=True)
    female_repeat_customers_sort = models.IntegerField(blank=True, null=True)
    new_customers_sort = models.IntegerField(blank=True, null=True)
    female_new_customers_sort = models.IntegerField(blank=True, null=True)
    sort_time = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_sort_backups'
        unique_together = (('goods_id', 'category', 'sort_time'),)


class CbdGoodsSortBank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    category = models.IntegerField(blank=True, null=True)
    sort_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_sort_bank'
        unique_together = (('bank_id', 'goods_id'),)


class CbdGoodsSortPreinstall(models.Model):
    pre_date = models.DateField(blank=True, null=True)
    pre_hour = models.PositiveIntegerField(blank=True, null=True)
    goods_id = models.PositiveIntegerField(blank=True, null=True)
    repeat_customers_sort = models.IntegerField(blank=True, null=True)
    female_repeat_customers_sort = models.IntegerField(blank=True, null=True)
    new_customers_sort = models.IntegerField(blank=True, null=True)
    female_new_customers_sort = models.IntegerField(blank=True, null=True)
    thirty_days_man_sort = models.IntegerField()
    thirty_days_woman_sort = models.IntegerField()
    category = models.PositiveIntegerField(blank=True, null=True)
    sort_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_sort_preinstall'
        unique_together = (('goods_id', 'category', 'pre_date', 'pre_hour'),)


class CbdGoodsStyle(models.Model):
    union_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    style_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_goods_style'


class CbdGoodsTag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    tag_name = models.CharField(max_length=50)
    tag_type = models.IntegerField(blank=True, null=True)
    click_num = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goods_tag'


class CbdGoodslog(models.Model):
    log_id = models.AutoField(primary_key=True)
    operate = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    operator = models.CharField(max_length=20, blank=True, null=True)
    group = models.CharField(max_length=20, blank=True, null=True)
    logtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_goodslog'


class CbdGroup(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=50)
    create_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()
    status = models.PositiveIntegerField()
    sort = models.PositiveSmallIntegerField()
    show = models.PositiveIntegerField()
    pid = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_group'


class CbdHistory(models.Model):
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_history'


class CbdHomeGoods(models.Model):
    goods_id = models.IntegerField()
    goods_no = models.CharField(max_length=50)
    special_id = models.IntegerField()
    statue = models.IntegerField()
    sort = models.IntegerField()
    create_time = models.IntegerField()
    create_id = models.IntegerField()
    create_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'cbd_home_goods'


class CbdHomeStyleSetting(models.Model):
    title = models.CharField(max_length=50)
    setting = models.TextField()
    status = models.IntegerField()
    add_time = models.PositiveIntegerField()
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    suit_sj_app = models.IntegerField(blank=True, null=True)
    suit_tm_app = models.IntegerField(blank=True, null=True)
    suit_yx_app = models.IntegerField(blank=True, null=True)
    suit_db_app = models.IntegerField(blank=True, null=True)
    suit_sj_xcx = models.IntegerField(blank=True, null=True)
    suit_yx_xcx = models.IntegerField(blank=True, null=True)
    suit_db_xcx = models.IntegerField(blank=True, null=True)
    earliest_version = models.CharField(max_length=12, blank=True, null=True)
    newest_version = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_home_style_setting'


class CbdHomeTips(models.Model):
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    target_url = models.CharField(max_length=255)
    bt_content = models.CharField(max_length=20)
    status = models.IntegerField()
    read_time = models.IntegerField()
    create_uid = models.BigIntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_home_tips'


class CbdHomeTplImgClickLog(models.Model):
    tpl_img_id = models.IntegerField()
    img_no = models.PositiveIntegerField()
    click_ip = models.CharField(max_length=15, blank=True, null=True)
    click_time = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_home_tpl_img_click_log'


class CbdHomeTplImgShowLog(models.Model):
    tpl_img_id = models.IntegerField()
    img_no = models.PositiveIntegerField()
    show_ip = models.CharField(max_length=15, blank=True, null=True)
    show_time = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_home_tpl_img_show_log'


class CbdHotGoodsCache(models.Model):
    goods_id = models.IntegerField()
    goods_bzno = models.CharField(max_length=50, blank=True, null=True)
    cate = models.IntegerField(blank=True, null=True)
    second_cate = models.IntegerField(blank=True, null=True)
    three_cate = models.IntegerField(blank=True, null=True)
    goods_type = models.IntegerField(blank=True, null=True)
    goods_name = models.CharField(max_length=200, blank=True, null=True)
    saletype = models.IntegerField(blank=True, null=True)
    open_time = models.IntegerField(blank=True, null=True)
    close_time = models.IntegerField(blank=True, null=True)
    label = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    createtime = models.IntegerField(blank=True, null=True)
    praisenum = models.IntegerField(blank=True, null=True)
    special_id = models.IntegerField(blank=True, null=True)
    salenum = models.IntegerField(blank=True, null=True)
    cached_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_hot_goods_cache'


class CbdHourConversion(models.Model):
    date = models.DateField(blank=True, null=True)
    date_hour = models.IntegerField(blank=True, null=True)
    order_count = models.IntegerField(blank=True, null=True)
    uv = models.IntegerField(blank=True, null=True)
    conversion = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_hour_conversion'


class CbdIdentityAuth(models.Model):
    user_id = models.BigIntegerField()
    true_name = models.CharField(max_length=50)
    card_no = models.CharField(max_length=50)
    card_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_identity_auth'


class CbdIdentityAuthLog(models.Model):
    user_id = models.BigIntegerField()
    last_date = models.DateField()
    today_count = models.IntegerField()
    total_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_identity_auth_log'


class CbdIdentityOfInviter(models.Model):
    user_id = models.BigIntegerField(unique=True)
    real_name = models.CharField(max_length=6)
    identity = models.CharField(max_length=18)
    create_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_identity_of_inviter'


class CbdImgfavs(models.Model):
    imgfavs_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(blank=True, null=True)
    img120_url = models.CharField(max_length=200, blank=True, null=True)
    img320_url = models.CharField(max_length=200, blank=True, null=True)
    img640_url = models.CharField(max_length=200, blank=True, null=True)
    img1080_url = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    is_cover = models.IntegerField(blank=True, null=True)
    is_visible = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    favs = models.IntegerField(blank=True, null=True)
    image_text = models.IntegerField(blank=True, null=True)
    img120_width = models.IntegerField(blank=True, null=True)
    img120_height = models.IntegerField(blank=True, null=True)
    img320_width = models.IntegerField(blank=True, null=True)
    img320_height = models.IntegerField(blank=True, null=True)
    img640_width = models.IntegerField(blank=True, null=True)
    img640_height = models.IntegerField(blank=True, null=True)
    img1080_width = models.IntegerField(blank=True, null=True)
    img1080_height = models.IntegerField(blank=True, null=True)
    spec_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_imgfavs'


class CbdIndexCount(models.Model):
    count_id = models.AutoField(primary_key=True)
    order_count = models.IntegerField(blank=True, null=True)
    sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reg_count = models.IntegerField(blank=True, null=True)
    new_user_order_count = models.IntegerField(blank=True, null=True)
    sale_goods_num = models.IntegerField(blank=True, null=True)
    new_up_goods_num = models.IntegerField(blank=True, null=True)
    wx_goods_num = models.IntegerField(blank=True, null=True)
    goods_count = models.IntegerField(blank=True, null=True)
    mkf_up_goods_count = models.IntegerField(blank=True, null=True)
    mkf_up_sku_count = models.IntegerField(blank=True, null=True)
    fbs_up_goods_count = models.IntegerField(blank=True, null=True)
    fbs_up_sku_count = models.IntegerField(blank=True, null=True)
    up_goods_count = models.IntegerField(blank=True, null=True)
    type_sale_goods_num = models.TextField(blank=True, null=True)
    count_date = models.DateField(blank=True, null=True)
    ave_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    old_orders_than = models.IntegerField(blank=True, null=True)
    seven_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    thirty_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    new_sale_than = models.IntegerField(blank=True, null=True)
    vx_sale_than = models.IntegerField(blank=True, null=True)
    nostock = models.IntegerField(blank=True, null=True)
    sale_user_num = models.IntegerField(blank=True, null=True)
    sale_goods_stock = models.IntegerField(blank=True, null=True)
    sale_goods_real_stock = models.IntegerField(blank=True, null=True)
    buy_two_user = models.IntegerField(blank=True, null=True)
    fbs_order_count = models.IntegerField(blank=True, null=True)
    fbs_sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    fbs_ave_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)
    floating_stocks = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    total_wealth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shopping_stock = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    invite_friends_num = models.IntegerField(blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ali_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wx_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    goods_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    active_user = models.IntegerField(blank=True, null=True)
    click_num = models.IntegerField(blank=True, null=True)
    return_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user_click_avg = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    special_num = models.IntegerField(blank=True, null=True)
    new_special_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_index_count'


class CbdIndexRecommendBrand(models.Model):
    recommend_id = models.AutoField(primary_key=True)
    recommend_brand_id = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_index_recommend_brand'


class CbdInformation(models.Model):
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=500)
    img_url = models.CharField(max_length=255)
    msg_type = models.PositiveIntegerField()
    special_id = models.IntegerField()
    send_type = models.PositiveIntegerField()
    send_time = models.PositiveIntegerField()
    user_type = models.PositiveIntegerField()
    is_cancel = models.PositiveIntegerField()
    is_send = models.PositiveIntegerField()
    push_status = models.IntegerField()
    push_time = models.PositiveIntegerField()
    jpush_msg_id = models.CharField(max_length=20)
    jpush_error_msg = models.CharField(max_length=255)
    jpush_error_code = models.IntegerField()
    add_time = models.IntegerField()
    update_time = models.DateTimeField()
    push_to = models.CharField(max_length=20)
    jump_target_kind = models.IntegerField()
    jump_target_value = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'cbd_information'


class CbdIosShortChain(models.Model):
    name = models.CharField(unique=True, max_length=100)
    url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'cbd_ios_short_chain'


class CbdKaSupplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    fbs_supplier_id = models.PositiveIntegerField()
    supplier_name = models.CharField(max_length=200)
    create_time = models.IntegerField()
    update_time = models.PositiveIntegerField()
    state = models.IntegerField()
    is_delete = models.PositiveIntegerField()
    remark = models.TextField()

    class Meta:
        managed = False
        db_table = 'cbd_ka_supplier'


class CbdKefuChat(models.Model):
    user_id = models.BigIntegerField()
    shop_id = models.IntegerField()
    staff_id = models.IntegerField()
    type = models.IntegerField()
    msg_id = models.CharField(unique=True, max_length=42)
    msg_time = models.IntegerField()
    msg_type = models.IntegerField()
    msg_content = models.TextField()
    received = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_kefu_chat'


class CbdKeywordsPhrases(models.Model):
    phrases = models.CharField(max_length=50)
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_keywords_phrases'


class CbdKeywordsWords(models.Model):
    phrases_id = models.IntegerField()
    words = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cbd_keywords_words'


class CbdLfActivity(models.Model):
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)
    is_close = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_lf_activity'


class CbdLfActivityDetail(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    goods = models.TextField(blank=True, null=True)
    special = models.TextField(blank=True, null=True)
    lf_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_lf_activity_detail'


class CbdListShowFields(models.Model):
    user_account = models.CharField(max_length=20, blank=True, null=True)
    show_fields = models.CharField(max_length=1000, blank=True, null=True)
    data_kind = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_list_show_fields'


class CbdLuckyBag(models.Model):
    bag_id = models.AutoField(primary_key=True)
    bag_spec_id = models.IntegerField(blank=True, null=True)
    pack_num = models.IntegerField(blank=True, null=True)
    random_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_lucky_bag'


class CbdLuckyBagDetail(models.Model):
    bag_id = models.IntegerField(blank=True, null=True)
    goods_no = models.CharField(max_length=100, blank=True, null=True)
    spec_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_lucky_bag_detail'


class CbdMakeMoneyGoods(models.Model):
    goods_id = models.IntegerField(unique=True)
    sort = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    tag_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_make_money_goods'


class CbdMakeMoneyGoodsPreSort(models.Model):
    category = models.PositiveIntegerField()
    pre_num = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    goods_id = models.PositiveIntegerField()
    sort_value = models.PositiveIntegerField()
    sort_time = models.PositiveIntegerField()
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_make_money_goods_pre_sort'


class CbdMakeMoneyGoodsSort(models.Model):
    sort_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    repeat_customers_sort = models.IntegerField(blank=True, null=True)
    female_repeat_customers_sort = models.IntegerField(blank=True, null=True)
    new_customers_sort = models.IntegerField(blank=True, null=True)
    female_new_customers_sort = models.IntegerField(blank=True, null=True)
    sort_time = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_make_money_goods_sort'
        unique_together = (('goods_id', 'category'),)


class CbdMakeMoneyGoodsSortBackups(models.Model):
    sort_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    repeat_customers_sort = models.IntegerField(blank=True, null=True)
    female_repeat_customers_sort = models.IntegerField(blank=True, null=True)
    new_customers_sort = models.IntegerField(blank=True, null=True)
    female_new_customers_sort = models.IntegerField(blank=True, null=True)
    sort_time = models.IntegerField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_make_money_goods_sort_backups'
        unique_together = (('goods_id', 'category', 'sort_time'),)


class CbdMakeMoneyGoodsSortBank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_make_money_goods_sort_bank'
        unique_together = (('bank_id', 'goods_id'), ('goods_id', 'category'),)


class CbdMakeMoneyGoodsTag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=15, blank=True, null=True)
    tag_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_make_money_goods_tag'


class CbdMallBargain(models.Model):
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    goods_num = models.PositiveIntegerField()
    crazy_price = models.DecimalField(max_digits=10, decimal_places=2)
    flash_price = models.DecimalField(max_digits=10, decimal_places=2)
    bargain_amount = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.PositiveIntegerField()
    expire_time = models.PositiveIntegerField()
    close_time = models.PositiveIntegerField()
    required_friend_num = models.PositiveIntegerField()
    joined_friend_num = models.PositiveIntegerField()
    order_id = models.BigIntegerField()
    is_finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_mall_bargain'


class CbdMallBargainDetail(models.Model):
    bargain_id = models.PositiveIntegerField()
    bargain_amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.IntegerField()
    account_openid = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_mall_bargain_detail'


class CbdMallBargainOpenAccount(models.Model):
    type = models.IntegerField()
    openid = models.CharField(max_length=60)
    nickname = models.CharField(max_length=50)
    head_portrait_url = models.TextField()
    add_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_mall_bargain_open_account'
        unique_together = (('type', 'openid'),)


class CbdMarketIndex(models.Model):
    keyword = models.CharField(unique=True, max_length=32)
    goods_ids = models.CharField(max_length=1800)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_market_index'


class CbdMarketSeckillOrderGoods(models.Model):
    goods_id = models.IntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_market_seckill_order_goods'


class CbdMarketingImport(models.Model):
    date = models.CharField(max_length=13, blank=True, null=True)
    agent_id = models.IntegerField()
    media_name = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=20, blank=True, null=True)
    consumed = models.IntegerField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    additional_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pct = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    roi = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_marketing_import'


class CbdMeeting(models.Model):
    id = models.IntegerField(primary_key=True)
    int = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_meeting'


class CbdMerchant(models.Model):
    fbs_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    link_man = models.CharField(max_length=20, blank=True, null=True)
    link_phone = models.CharField(max_length=20, blank=True, null=True)
    link_email = models.CharField(max_length=50, blank=True, null=True)
    category_ids = models.CharField(max_length=50, blank=True, null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    shopkeeper_name = models.CharField(max_length=50, blank=True, null=True)
    corporation_name = models.CharField(max_length=50, blank=True, null=True)
    certificates_id_type = models.IntegerField(blank=True, null=True)
    certificates_id = models.CharField(max_length=50, blank=True, null=True)
    certificates_type = models.IntegerField(blank=True, null=True)
    certificates_start_time = models.DateTimeField(blank=True, null=True)
    certificates_end_time = models.DateTimeField(blank=True, null=True)
    certificates_image_before = models.CharField(max_length=200, blank=True, null=True)
    certificates_image_after = models.CharField(max_length=200, blank=True, null=True)
    certificates_image_full = models.CharField(max_length=200, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_province_id = models.IntegerField(blank=True, null=True)
    company_province_name = models.CharField(max_length=50, blank=True, null=True)
    company_city_id = models.IntegerField(blank=True, null=True)
    company_city_name = models.CharField(max_length=50, blank=True, null=True)
    company_district_id = models.IntegerField(blank=True, null=True)
    company_district_name = models.CharField(max_length=50, blank=True, null=True)
    company_address = models.CharField(max_length=300, blank=True, null=True)
    credit_code = models.CharField(max_length=200, blank=True, null=True)
    company_image_business_licence = models.CharField(max_length=300, blank=True, null=True)
    company_image_account_opening_permit = models.CharField(max_length=300, blank=True, null=True)
    company_image_taxpayer_certificate = models.CharField(max_length=300, blank=True, null=True)
    company_trademark_type = models.IntegerField(blank=True, null=True)
    company_trademark_no = models.CharField(max_length=50, blank=True, null=True)
    company_trademark_image = models.TextField(blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    refuse_reason = models.CharField(max_length=500, blank=True, null=True)
    add_time = models.PositiveIntegerField(blank=True, null=True)
    last_update_time = models.PositiveIntegerField(blank=True, null=True)
    audit_time = models.PositiveIntegerField(blank=True, null=True)
    is_paid = models.IntegerField()
    is_signed = models.IntegerField()
    sync_status = models.IntegerField()
    reg_type = models.IntegerField()
    bd_names = models.CharField(max_length=20, blank=True, null=True)
    business_names = models.CharField(max_length=20, blank=True, null=True)
    operate_names = models.CharField(max_length=20, blank=True, null=True)
    company_trademark_json = models.TextField(blank=True, null=True)
    pay_state = models.IntegerField(blank=True, null=True)
    aptitude = models.IntegerField(blank=True, null=True)
    merchant_img = models.CharField(max_length=160, blank=True, null=True)
    shop_desc = models.CharField(max_length=600, blank=True, null=True)
    fbs_key_id = models.IntegerField(blank=True, null=True)
    agreement_read = models.IntegerField(blank=True, null=True)
    qq_number = models.CharField(max_length=15, blank=True, null=True)
    bd_mobile = models.CharField(max_length=11, blank=True, null=True)
    main_goods = models.CharField(max_length=1000, blank=True, null=True)
    custom_service_phone = models.CharField(max_length=20, blank=True, null=True)
    personal_name = models.CharField(max_length=10)
    personal_business_licence_name = models.CharField(max_length=20)
    personal_trademark_no = models.CharField(max_length=20)
    personal_type = models.CharField(max_length=20)
    personal_comprise = models.CharField(max_length=50)
    personal_register_time = models.PositiveIntegerField()
    personal_business_range = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cbd_merchant'


class CbdMerchantChangeApply(models.Model):
    fbs_supplier_id = models.PositiveIntegerField(unique=True)
    change_type = models.PositiveIntegerField()
    change_audit_state = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_merchant_change_apply'


class CbdMerchantCount(models.Model):
    supplier_id = models.IntegerField()
    sale_num = models.IntegerField()
    goods_count = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_merchant_count'


class CbdMerchantRecommendGoods(models.Model):
    supplier_id = models.IntegerField()
    goods_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_merchant_recommend_goods'


class CbdMerchantShopGoods(models.Model):
    supplier_id = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    goods_sort = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_merchant_shop_goods'


class CbdMerchantShopList(models.Model):
    kind = models.IntegerField()
    supplier_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_merchant_shop_list'


class CbdMerchantSyncLog(models.Model):
    merchant_id = models.IntegerField(blank=True, null=True)
    sync_kind = models.IntegerField(blank=True, null=True)
    sync_status = models.IntegerField(blank=True, null=True)
    sync_msg = models.TextField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    result_msg = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_merchant_sync_log'


class CbdMkfFbsApiLog(models.Model):
    queue = models.CharField(max_length=255, blank=True, null=True)
    batch_no = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    json = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_mkf_fbs_api_log'


class CbdMkfFbsSyncLog(models.Model):
    queue = models.CharField(max_length=50)
    msg_data = models.TextField(blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_mkf_fbs_sync_log'


class CbdMkfset(models.Model):
    set_id = models.AutoField(primary_key=True)
    setkey = models.CharField(max_length=30, blank=True, null=True)
    setvalue = models.CharField(max_length=200, blank=True, null=True)
    setvalue1 = models.CharField(max_length=100, blank=True, null=True)
    setvalue2 = models.CharField(max_length=200, blank=True, null=True)
    setvalue3 = models.CharField(max_length=200, blank=True, null=True)
    createtime = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_mkfset'


class CbdMlOrder(models.Model):
    ml_id = models.AutoField(primary_key=True)
    order_no = models.CharField(max_length=40)
    user_id = models.BigIntegerField()
    amount = models.FloatField()
    level = models.SmallIntegerField()
    payment_id = models.IntegerField(blank=True, null=True)
    pay_state = models.PositiveIntegerField(blank=True, null=True)
    billno = models.CharField(max_length=60, blank=True, null=True)
    paytime = models.IntegerField(blank=True, null=True)
    payname = models.CharField(max_length=100, blank=True, null=True)
    payamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.IntegerField()
    effective_time = models.PositiveIntegerField(blank=True, null=True)
    order_state = models.IntegerField()
    seller_id = models.CharField(max_length=50, blank=True, null=True)
    discount = models.DecimalField(max_digits=3, decimal_places=1)
    default_discount = models.DecimalField(max_digits=3, decimal_places=1)
    payno = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_ml_order'


class CbdMlOrderDuplicatePay(models.Model):
    order_id = models.BigIntegerField()
    order_no = models.CharField(max_length=50)
    billno = models.CharField(max_length=60)
    payamount = models.DecimalField(max_digits=10, decimal_places=2)
    paytime = models.IntegerField()
    paycode = models.CharField(max_length=50)
    payname = models.CharField(max_length=100)
    seller_id = models.CharField(max_length=50)
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_ml_order_duplicate_pay'


class CbdModuleAction(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    module_name = models.CharField(max_length=32)
    action_name = models.CharField(max_length=32)
    introduce = models.CharField(max_length=128)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_module_action'


class CbdModuleActionCount(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    ma_id = models.PositiveSmallIntegerField()
    hits = models.PositiveIntegerField()
    click_time = models.IntegerField()
    create_time = models.IntegerField()
    module_name = models.CharField(max_length=32)
    action_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cbd_module_action_count'


class CbdModuleActionDetail(models.Model):
    ma_id = models.PositiveSmallIntegerField()
    username = models.CharField(max_length=50)
    click_time = models.IntegerField()
    module_name = models.CharField(max_length=32)
    action_name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'cbd_module_action_detail'


class CbdNewCustomerBgBak(models.Model):
    tab_type = models.IntegerField()
    tab_cate_id = models.IntegerField(blank=True, null=True)
    img_url = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_new_customer_bg_bak'


class CbdNewCustomerCate(models.Model):
    cate_name = models.CharField(max_length=25, blank=True, null=True)
    tab_type = models.PositiveIntegerField(blank=True, null=True)
    tab_sort = models.IntegerField(blank=True, null=True)
    bg_color = models.CharField(max_length=10, blank=True, null=True)
    add_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_new_customer_cate'


class CbdNewCustomerGoods(models.Model):
    goods_id = models.PositiveIntegerField(blank=True, null=True)
    tab_type = models.PositiveIntegerField(blank=True, null=True)
    tab_cate_id = models.PositiveIntegerField(blank=True, null=True)
    goods_sort = models.IntegerField(blank=True, null=True)
    add_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_new_customer_goods'


class CbdNewCustomerLog(models.Model):
    tab_type = models.PositiveIntegerField(blank=True, null=True)
    operate_type = models.PositiveIntegerField(blank=True, null=True)
    content = models.CharField(max_length=1000, blank=True, null=True)
    operator = models.CharField(max_length=30, blank=True, null=True)
    add_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_new_customer_log'


class CbdNewCustomerPriceBak(models.Model):
    tab_type = models.IntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supplier_bear_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_new_customer_price_bak'


class CbdNewCustomerWinRecord(models.Model):
    user_id = models.BigIntegerField()
    win_type = models.IntegerField()
    win_content = models.CharField(max_length=255)
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_new_customer_win_record'


class CbdNewUserCoupon(models.Model):
    coupon_name = models.CharField(max_length=10, blank=True, null=True)
    coupon_type = models.IntegerField(blank=True, null=True)
    preferential_type = models.IntegerField(blank=True, null=True)
    use_range = models.IntegerField(blank=True, null=True)
    give_group = models.IntegerField(blank=True, null=True)
    expiry_date = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_new_user_coupon'


class CbdNewbiePrice(models.Model):
    newbies_activity_id = models.IntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    newbie_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cbd_newbie_price'
        unique_together = (('newbies_activity_id', 'goods_id', 'spec_id'),)


class CbdNewbiesActivity(models.Model):
    goods_id = models.TextField()
    crazy_price = models.TextField()
    activity_type = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_newbies_activity'


class CbdNewuserPrice(models.Model):
    newbies_activity_id = models.IntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    newuser_price = models.DecimalField(max_digits=10, decimal_places=2)
    newuser_price_app = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cbd_newuser_price'
        unique_together = (('newbies_activity_id', 'goods_id', 'spec_id'),)


class CbdNode(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    sort = models.PositiveSmallIntegerField(blank=True, null=True)
    pid = models.PositiveSmallIntegerField()
    level = models.PositiveIntegerField()
    type = models.IntegerField()
    group_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_node'


class CbdOmsDecodeLog(models.Model):
    queue = models.CharField(max_length=50, blank=True, null=True)
    string = models.TextField(blank=True, null=True)
    serial_no = models.CharField(max_length=50, blank=True, null=True)
    is_verify = models.IntegerField(blank=True, null=True)
    decode_array = models.TextField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_oms_decode_log'


class CbdOneMarket(models.Model):
    market_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField()
    user_id = models.BigIntegerField()
    order_no = models.CharField(max_length=40, blank=True, null=True)
    assistant_id = models.BigIntegerField(blank=True, null=True)
    state = models.IntegerField()
    create_time = models.IntegerField()
    assistant_time = models.IntegerField(blank=True, null=True)
    pay_time = models.IntegerField(blank=True, null=True)
    share_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_one_market'


class CbdOneYuanData(models.Model):
    data_date = models.DateField(unique=True, blank=True, null=True)
    start_buy_order_num = models.PositiveIntegerField(blank=True, null=True)
    success_buy_order_num = models.PositiveIntegerField(blank=True, null=True)
    buy_success_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_share_order_num = models.PositiveIntegerField(blank=True, null=True)
    order_start_share_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_share_total_num = models.PositiveIntegerField(blank=True, null=True)
    avg_share_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    share_avg_click_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    buy_home_page_uv = models.PositiveIntegerField(blank=True, null=True)
    new_user_uv = models.PositiveIntegerField(blank=True, null=True)
    old_user_uv = models.PositiveIntegerField(blank=True, null=True)
    reg_user_num = models.PositiveIntegerField(blank=True, null=True)
    reg_user_order_num = models.PositiveIntegerField(blank=True, null=True)
    new_pay_user_num = models.PositiveIntegerField(blank=True, null=True)
    new_pay_kd = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    new_pay_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_supply_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_group_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reg_supply_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    reg_group_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_supply_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pay_group_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_a_buy_order_num = models.PositiveIntegerField(blank=True, null=True)
    start_b_buy_order_num = models.PositiveIntegerField(blank=True, null=True)
    success_a_buy_order_num = models.PositiveIntegerField(blank=True, null=True)
    success_b_buy_order_num = models.PositiveIntegerField(blank=True, null=True)
    success_a_buy_order_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    success_b_buy_order_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_share_a_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_share_b_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    start_share_a_total_num = models.PositiveIntegerField(blank=True, null=True)
    start_share_b_total_num = models.PositiveIntegerField(blank=True, null=True)
    avg_share_a_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    avg_share_b_num = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    update_time = models.PositiveIntegerField()
    app_launch_order_num = models.PositiveIntegerField(blank=True, null=True)
    wechat_launch_order_num = models.PositiveIntegerField(blank=True, null=True)
    launch_one_yuan_order_num = models.PositiveIntegerField(blank=True, null=True)
    launch_five_yuan_order_num = models.PositiveIntegerField(blank=True, null=True)
    launch_ten_yuan_order_num = models.PositiveIntegerField(blank=True, null=True)
    app_launch_success_order_num = models.PositiveIntegerField(blank=True, null=True)
    wechat_launch_success_order_num = models.PositiveIntegerField(blank=True, null=True)
    one_yuan_seccess_order_num = models.PositiveIntegerField(blank=True, null=True)
    five_yuan_seccess_order_num = models.PositiveIntegerField(blank=True, null=True)
    ten_yuan_seccess_order_num = models.PositiveIntegerField(blank=True, null=True)
    one_yuan_order_seccess_rate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    five_yuan_order_seccess_rate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ten_yuan_order_seccess_rate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    start_one_yuan_share_order_num = models.PositiveIntegerField(blank=True, null=True)
    start_five_yuan_share_order_num = models.PositiveIntegerField(blank=True, null=True)
    start_ten_yuan_share_order_num = models.PositiveIntegerField(blank=True, null=True)
    one_yuan_order_start_rate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    five_yuan_order_start_rate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ten_yuan_order_start_rate = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    one_yuan_home_page_uv = models.PositiveIntegerField(blank=True, null=True)
    five_yuan_home_page_uv = models.PositiveIntegerField(blank=True, null=True)
    ten_yuan_home_page_uv = models.PositiveIntegerField(blank=True, null=True)
    total_order_subsidy_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    reg_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    pay_cost = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_one_yuan_data'


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
    is_open_vip = models.PositiveIntegerField()
    open_vip_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_group = models.PositiveIntegerField()
    fight_id = models.PositiveIntegerField()
    cut_id = models.PositiveIntegerField()
    is_newer = models.PositiveIntegerField()
    boost_id = models.IntegerField()
    shares_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
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


class CbdOrderActivityStock(models.Model):
    order_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    use_stock = models.DecimalField(max_digits=10, decimal_places=1)
    is_return = models.PositiveIntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_order_activity_stock'


class CbdOrderBargain(models.Model):
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    goods_num = models.PositiveIntegerField()
    shop_price = models.DecimalField(max_digits=10, decimal_places=2)
    flash_price = models.DecimalField(max_digits=10, decimal_places=2)
    bargain_amount = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.PositiveIntegerField()
    close_time = models.PositiveIntegerField()
    required_friend_num = models.PositiveIntegerField()
    joined_friend_num = models.PositiveIntegerField()
    is_paid = models.IntegerField()
    is_finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_order_bargain'


class CbdOrderBargainDetail(models.Model):
    bargain_id = models.PositiveIntegerField()
    bargain_amount = models.DecimalField(max_digits=10, decimal_places=2)
    account_type = models.IntegerField()
    account_openid = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_order_bargain_detail'


class CbdOrderCheckOmsLog(models.Model):
    detail_no = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    result = models.CharField(max_length=20, blank=True, null=True)
    msg = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_order_check_oms_log'


class CbdOrderCompensateLog(models.Model):
    user_id = models.BigIntegerField()
    detail_no = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField(blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_order_compensate_log'


class CbdOrderCopyLog(models.Model):
    order_id = models.BigIntegerField()
    detail_no = models.CharField(max_length=50)
    new_order_id = models.BigIntegerField()
    new_detail_no = models.CharField(max_length=50)
    operator = models.CharField(max_length=50)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_order_copy_log'


class CbdOrderCountHour(models.Model):
    date = models.DateField()
    hour = models.IntegerField()
    os = models.CharField(max_length=10)
    total_order_num = models.IntegerField()
    total_pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    avg_pay_amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_order_count_hour'
        unique_together = (('date', 'hour', 'os'),)


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


class CbdOrderDuplicatePay(models.Model):
    order_id = models.BigIntegerField()
    order_no = models.CharField(max_length=50)
    billno = models.CharField(max_length=60)
    payamount = models.DecimalField(max_digits=10, decimal_places=2)
    paytime = models.IntegerField()
    paycode = models.CharField(max_length=50)
    payname = models.CharField(max_length=100)
    seller_id = models.CharField(max_length=50)
    add_time = models.IntegerField()
    is_launch = models.IntegerField(blank=True, null=True)
    launchtime = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    result_log = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_order_duplicate_pay'


class CbdOrderDuplicatePayLog(models.Model):
    duplicate_pay_id = models.IntegerField()
    param_log = models.TextField(blank=True, null=True)
    result_log = models.TextField(blank=True, null=True)
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_order_duplicate_pay_log'


class CbdOrderFight(models.Model):
    fight_id = models.AutoField(primary_key=True)
    order_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    avatar = models.CharField(max_length=255)
    fight_num = models.SmallIntegerField()
    fight_price = models.DecimalField(max_digits=10, decimal_places=2)
    update_num = models.SmallIntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    status = models.IntegerField()
    status_share = models.IntegerField()
    goods_id = models.IntegerField()
    goods_no = models.CharField(max_length=30)
    detail_no = models.CharField(max_length=50)
    is_send = models.IntegerField()
    last_time = models.IntegerField()
    goods_num = models.IntegerField()
    is_send_waitgroup = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_order_fight'


class CbdOrderFightCollage(models.Model):
    fight_id = models.IntegerField()
    order_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    avatar = models.CharField(max_length=255)
    identity = models.IntegerField()
    create_time = models.IntegerField()
    goods_id = models.IntegerField()
    goods_no = models.CharField(max_length=30)
    detail_no = models.CharField(max_length=50)
    is_update = models.IntegerField()
    status = models.IntegerField()
    is_send = models.IntegerField()
    last_time = models.IntegerField()
    number = models.IntegerField()
    repeat_time = models.IntegerField()
    push_cut_status = models.IntegerField()
    is_has_so_code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_order_fight_collage'


class CbdOrderFreight(models.Model):
    f_id = models.AutoField(primary_key=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    detail_no = models.CharField(max_length=50)
    shop_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    province = models.SmallIntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    default_freight = models.DecimalField(max_digits=10, decimal_places=2)
    incr_freight = models.DecimalField(max_digits=10, decimal_places=2)
    tpl_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_order_freight'


class CbdOrderGoodsSource(models.Model):
    od_id = models.BigIntegerField(primary_key=True)
    goods_source = models.CharField(max_length=100, blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)
    device_id = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'cbd_order_goods_source'


class CbdOrderOmsLog(models.Model):
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    so_code = models.CharField(max_length=30, blank=True, null=True)
    outer_order_code = models.CharField(max_length=50, blank=True, null=True)
    op_type = models.IntegerField(blank=True, null=True)
    op_time = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    trans_code = models.CharField(max_length=255, blank=True, null=True)
    trans_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    is_fbs = models.IntegerField(blank=True, null=True)
    send_times = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_order_oms_log'


class CbdOrderSupplierFreight(models.Model):
    order_id = models.BigIntegerField(blank=True, null=True)
    detail_no = models.CharField(max_length=60, blank=True, null=True)
    fbs_supplier_id = models.IntegerField(blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    province = models.SmallIntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    json_freight_fee = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_order_supplier_freight'


class CbdOrdernumLog(models.Model):
    order_id = models.BigIntegerField(blank=True, null=True)
    spec_id = models.PositiveIntegerField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)
    ordernum = models.IntegerField(blank=True, null=True)
    stocknum = models.IntegerField(blank=True, null=True)
    sql = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.PositiveIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_ordernum_log'


class CbdOwnOreConfig(models.Model):
    jump_type = models.IntegerField(unique=True, blank=True, null=True)
    jump_value = models.CharField(max_length=255, blank=True, null=True)
    operator = models.CharField(max_length=20, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_own_ore_config'


class CbdOwnOreGoods(models.Model):
    goods_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    sort = models.PositiveIntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_own_ore_goods'


class CbdOwnOrePrize(models.Model):
    goods_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    sort = models.PositiveIntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_own_ore_prize'


class CbdOwnOreUserPrize(models.Model):
    goods_id = models.PositiveIntegerField(blank=True, null=True)
    spec_id = models.PositiveIntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    create_time = models.PositiveIntegerField(blank=True, null=True)
    update_time = models.PositiveIntegerField(blank=True, null=True)
    game_finish_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_own_ore_user_prize'


class CbdPackGoods(models.Model):
    gp_id = models.AutoField(primary_key=True)
    pack_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    spec_id = models.IntegerField(blank=True, null=True)
    pack_spec_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_pack_goods'


class CbdPackOms(models.Model):
    pack_spec_id = models.IntegerField(blank=True, null=True)
    goods_no = models.CharField(max_length=30, blank=True, null=True)
    spec_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_pack_oms'


class CbdPageCodeDesc(models.Model):
    code_type = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    code_desc = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_page_code_desc'


class CbdPartitionsActivity(models.Model):
    img_name1 = models.CharField(max_length=500, blank=True, null=True)
    img_name2 = models.CharField(max_length=255, blank=True, null=True)
    img_name3 = models.CharField(max_length=255, blank=True, null=True)
    img_name4 = models.CharField(max_length=255, blank=True, null=True)
    img_name5 = models.CharField(max_length=255, blank=True, null=True)
    img_name6 = models.CharField(max_length=255, blank=True, null=True)
    img_name7 = models.CharField(max_length=500, blank=True, null=True)
    brand_ids = models.CharField(max_length=500, blank=True, null=True)
    listimg_pic1 = models.TextField(blank=True, null=True)
    listimg_pic2 = models.CharField(max_length=255, blank=True, null=True)
    listimg_pic3 = models.CharField(max_length=255, blank=True, null=True)
    listimg_pic4 = models.CharField(max_length=255, blank=True, null=True)
    listimg_pic5 = models.CharField(max_length=255, blank=True, null=True)
    listimg_pic6 = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    goods_ids = models.CharField(max_length=500, blank=True, null=True)
    cate_ids = models.CharField(max_length=500, blank=True, null=True)
    source_goods = models.TextField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    listimg_pic7 = models.CharField(max_length=255, blank=True, null=True)
    is_visible_app = models.IntegerField(blank=True, null=True)
    is_visible_xcx = models.IntegerField(blank=True, null=True)
    is_visible_ouch_app = models.IntegerField(blank=True, null=True)
    is_visible_ouch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_partitions_activity'


class CbdPartitionsActivityNew(models.Model):
    img_name1 = models.CharField(max_length=500, blank=True, null=True)
    img_name2 = models.CharField(max_length=255, blank=True, null=True)
    img_name3 = models.CharField(max_length=255, blank=True, null=True)
    img_name4 = models.CharField(max_length=255, blank=True, null=True)
    img_name5 = models.CharField(max_length=255, blank=True, null=True)
    img_name6 = models.CharField(max_length=255, blank=True, null=True)
    img_name7 = models.CharField(max_length=500, blank=True, null=True)
    brand_ids = models.CharField(max_length=500, blank=True, null=True)
    listimg_pic1 = models.TextField(blank=True, null=True)
    listimg_pic2 = models.CharField(max_length=255, blank=True, null=True)
    listimg_pic3 = models.CharField(max_length=255, blank=True, null=True)
    listimg_pic4 = models.CharField(max_length=255, blank=True, null=True)
    listimg_pic5 = models.CharField(max_length=255, blank=True, null=True)
    listimg_pic6 = models.CharField(max_length=255, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    goods_ids = models.CharField(max_length=500, blank=True, null=True)
    cate_ids = models.CharField(max_length=500, blank=True, null=True)
    source_goods = models.TextField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    listimg_pic7 = models.CharField(max_length=255, blank=True, null=True)
    is_visible_app = models.IntegerField(blank=True, null=True)
    is_visible_xcx = models.IntegerField(blank=True, null=True)
    is_visible_ouch_app = models.IntegerField(blank=True, null=True)
    is_visible_ouch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_partitions_activity_new'


class CbdPartitionsActivityPagecode(models.Model):
    activity_type = models.IntegerField()
    pic_level = models.IntegerField(blank=True, null=True)
    page_code = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_partitions_activity_pagecode'


class CbdPayment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    pay_code = models.CharField(max_length=20, blank=True, null=True)
    pay_name = models.CharField(max_length=120, blank=True, null=True)
    pay_fee = models.CharField(max_length=10, blank=True, null=True)
    pay_desc = models.TextField(blank=True, null=True)
    pay_order = models.IntegerField(blank=True, null=True)
    pay_config = models.TextField(blank=True, null=True)
    enabled = models.IntegerField(blank=True, null=True)
    is_cod = models.IntegerField(blank=True, null=True)
    is_online = models.IntegerField(blank=True, null=True)
    is_app = models.IntegerField(blank=True, null=True)
    is_wap = models.IntegerField(blank=True, null=True)
    is_web = models.IntegerField(blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_payment'


class CbdPersonalDepositOrder(models.Model):
    pd_id = models.AutoField(primary_key=True)
    order_no = models.CharField(max_length=40)
    user_id = models.BigIntegerField()
    amount = models.FloatField()
    store_application = models.IntegerField()
    payment_id = models.IntegerField(blank=True, null=True)
    pay_state = models.PositiveIntegerField(blank=True, null=True)
    billno = models.CharField(max_length=60, blank=True, null=True)
    paytime = models.IntegerField(blank=True, null=True)
    payname = models.CharField(max_length=100, blank=True, null=True)
    payamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.IntegerField()
    order_state = models.IntegerField()
    seller_id = models.CharField(max_length=50, blank=True, null=True)
    payno = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_personal_deposit_order'


class CbdPopuTest(models.Model):
    idfa = models.CharField(max_length=255)
    idfa_md5 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cbd_popu_test'


class CbdPopularize(models.Model):
    popu_id = models.AutoField(primary_key=True)
    click_ip = models.CharField(max_length=20, blank=True, null=True)
    user_code = models.CharField(max_length=100, blank=True, null=True)
    spid = models.CharField(max_length=20, blank=True, null=True)
    mac = models.CharField(max_length=20, blank=True, null=True)
    mac_md5 = models.CharField(max_length=32, blank=True, null=True)
    idfa = models.CharField(max_length=50, blank=True, null=True)
    idfa_md5 = models.CharField(max_length=32, blank=True, null=True)
    device_id = models.CharField(max_length=120, blank=True, null=True)
    udid = models.CharField(max_length=50, blank=True, null=True)
    app_code = models.CharField(max_length=20, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    click_time = models.IntegerField(blank=True, null=True)
    is_action = models.IntegerField(blank=True, null=True)
    action_time = models.IntegerField(blank=True, null=True)
    action_ip = models.CharField(max_length=20, blank=True, null=True)
    app_version = models.CharField(max_length=20, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    sys = models.IntegerField(blank=True, null=True)
    click_id = models.CharField(max_length=24, blank=True, null=True)
    callback_url = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_popularize'


class CbdPopularizeBaidu(models.Model):
    user_id = models.BigIntegerField()
    ua = models.CharField(max_length=150)
    click_id = models.CharField(max_length=100)
    ts = models.CharField(max_length=30)
    create_time = models.CharField(max_length=30)
    idfa = models.CharField(unique=True, max_length=50)
    callback_url = models.CharField(max_length=200)
    is_action = models.SmallIntegerField()
    action_time = models.IntegerField(blank=True, null=True)
    action_ip = models.CharField(max_length=30, blank=True, null=True)
    action_type = models.CharField(max_length=20, blank=True, null=True)
    sign = models.CharField(max_length=200)
    pid = models.CharField(max_length=50)
    aid = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    os = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cbd_popularize_baidu'


class CbdPopularizeFreeIdfa(models.Model):
    idfa = models.CharField(unique=True, max_length=50)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_popularize_free_idfa'


class CbdPopularizeLog(models.Model):
    popu_id = models.PositiveIntegerField()
    popu_data = models.CharField(max_length=1000)
    act = models.IntegerField()
    curl_url = models.CharField(max_length=1000)
    curl_response = models.CharField(max_length=255)
    curl_http_code = models.IntegerField()
    curl_error = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_popularize_log'


class CbdPopularizeRebateLog(models.Model):
    popu_id = models.PositiveIntegerField()
    popu_data = models.TextField(blank=True, null=True)
    curl_response = models.CharField(max_length=255)
    curl_http_code = models.IntegerField()
    curl_error = models.CharField(max_length=255)
    conv_type = models.CharField(max_length=50)
    source = models.CharField(max_length=30)
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_popularize_rebate_log'


class CbdPopularizeRebateSite(models.Model):
    advertiser_id = models.CharField(max_length=100)
    user_id = models.BigIntegerField()
    app_id = models.CharField(max_length=100)
    app_type = models.CharField(max_length=30)
    click_id = models.CharField(max_length=100)
    click_time = models.CharField(max_length=30)
    idfa_md5 = models.CharField(unique=True, max_length=50)
    source = models.CharField(max_length=50)
    is_action = models.SmallIntegerField()
    action_time = models.IntegerField(blank=True, null=True)
    action_ip = models.CharField(max_length=30, blank=True, null=True)
    action_type = models.CharField(max_length=20, blank=True, null=True)
    return_id = models.IntegerField()
    order_conv_type = models.CharField(max_length=30, blank=True, null=True)
    order_id = models.BigIntegerField()
    reg_time = models.IntegerField(blank=True, null=True)
    pay_time = models.IntegerField(blank=True, null=True)
    return_time = models.IntegerField(blank=True, null=True)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    return_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_popularize_rebate_site'


class CbdPraiseGoods(models.Model):
    praise_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField(blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_praise_goods'


class CbdPriceChange(models.Model):
    goods_id = models.IntegerField(blank=True, null=True)
    goods_no = models.CharField(max_length=60, blank=True, null=True)
    supply_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_price_change'


class CbdPromotionCost(models.Model):
    data_date = models.DateField(unique=True, blank=True, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_promotion_cost'


class CbdPromotionGoodsSort(models.Model):
    goods_id = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_promotion_goods_sort'


class CbdPullnewDoleCoupon(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_pullnew_dole_coupon'


class CbdPushGoodsSaleRank(models.Model):
    data_date = models.DateField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    sale_num_14d = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_push_goods_sale_rank'


class CbdPushTest(models.Model):
    activity_name = models.CharField(max_length=10, blank=True, null=True)
    user_ids = models.CharField(max_length=225, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_push_test'


class CbdPushUserGoodsList(models.Model):
    user_id = models.BigIntegerField(unique=True, blank=True, null=True)
    goods_id_rule1 = models.IntegerField(blank=True, null=True)
    goods_id_rule2 = models.IntegerField(blank=True, null=True)
    goods_id_rule3 = models.IntegerField(blank=True, null=True)
    goods_id_rule4 = models.IntegerField(blank=True, null=True)
    goods_id_rule5 = models.IntegerField(blank=True, null=True)
    goods_id_rule6 = models.IntegerField(blank=True, null=True)
    goods_id_rule7 = models.IntegerField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_push_user_goods_list'


class CbdQualityMonitor(models.Model):
    is_visible_tjj = models.IntegerField()
    name = models.CharField(max_length=10)
    head_img = models.CharField(max_length=150)
    level = models.IntegerField()
    times = models.SmallIntegerField()
    operator = models.CharField(max_length=5, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_quality_monitor'


class CbdQualityMonitorGoods(models.Model):
    goods_id = models.IntegerField()
    monitor_id = models.IntegerField()
    keywords = models.CharField(max_length=20)
    resume = models.CharField(max_length=80)
    model_id = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    title = models.CharField(max_length=20)
    group = models.IntegerField()
    star = models.FloatField()
    status = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_quality_monitor_goods'


class CbdQualityMonitorSource(models.Model):
    goods_id = models.IntegerField()
    source_type = models.IntegerField()
    source_value = models.TextField()
    sort = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_quality_monitor_source'


class CbdQualityMuseumCate(models.Model):
    cate_name = models.CharField(max_length=10)
    goods_count = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    operator = models.CharField(max_length=30)
    sort = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_quality_museum_cate'


class CbdQualityMuseumGoods(models.Model):
    cate_id = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    goods_name = models.CharField(max_length=200)
    goods_pic = models.CharField(max_length=200)
    words = models.CharField(max_length=30)
    tag = models.CharField(max_length=10)
    sort = models.IntegerField()
    operator = models.CharField(max_length=30)
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_quality_museum_goods'
        unique_together = (('cate_id', 'goods_id'),)


class CbdQuestionResult(models.Model):
    user_id = models.BigIntegerField(unique=True)
    sex = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    job = models.PositiveIntegerField()
    income = models.PositiveIntegerField()
    focus_point = models.PositiveIntegerField()
    hobby = models.PositiveIntegerField()
    suggestion = models.CharField(max_length=500)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_question_result'


class CbdRate(models.Model):
    date_str = models.CharField(max_length=15, blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_rate'


class CbdReference(models.Model):
    reference_id = models.AutoField(primary_key=True)
    reference_name = models.CharField(max_length=50)
    reference_mobile = models.CharField(max_length=11)
    province_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=50, blank=True, null=True)
    state = models.IntegerField(blank=True, null=True)
    reg_num = models.IntegerField(blank=True, null=True)
    role_type = models.IntegerField(blank=True, null=True)
    qr_type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_reference'


class CbdReferenceGroup(models.Model):
    group_id = models.AutoField(primary_key=True)
    province_id = models.IntegerField()
    city_id = models.IntegerField()
    province_name = models.CharField(max_length=50, blank=True, null=True)
    city_name = models.CharField(max_length=50, blank=True, null=True)
    group_name = models.CharField(max_length=50, blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_reference_group'


class CbdReferenceRegion(models.Model):
    reference_id = models.IntegerField(blank=True, null=True)
    province_id = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_reference_region'


class CbdReferrerLog(models.Model):
    user_id = models.BigIntegerField()
    tel = models.CharField(max_length=20)
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_referrer_log'


class CbdRefund(models.Model):
    refund_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    order_no = models.CharField(max_length=40)
    billno = models.CharField(max_length=60)
    order_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_no = models.CharField(max_length=40)
    app_id = models.CharField(max_length=32)
    mch_id = models.CharField(max_length=32)
    payment_type = models.CharField(max_length=32)
    return_refund_fee = models.DecimalField(max_digits=10, decimal_places=2)
    return_code = models.CharField(max_length=16)
    return_msg = models.CharField(max_length=128)
    refund_time = models.IntegerField()
    refund_status = models.IntegerField()
    create_time = models.IntegerField()
    batch_no = models.CharField(max_length=50, blank=True, null=True)
    refund_send_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_refund'


class CbdRefuseRegion(models.Model):
    province = models.CharField(max_length=10, blank=True, null=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    county = models.CharField(max_length=10, blank=True, null=True)
    operator = models.CharField(max_length=10, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_refuse_region'


class CbdRegionFreightFee(models.Model):
    template_name = models.CharField(max_length=50, blank=True, null=True)
    region_fee = models.CharField(max_length=500, blank=True, null=True)
    fbs_supplier_id = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    set_type = models.IntegerField(blank=True, null=True)
    partial_all = models.IntegerField(blank=True, null=True)
    not_ship = models.CharField(max_length=500, blank=True, null=True)
    cover_region = models.CharField(max_length=500, blank=True, null=True)
    piece_weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_region_freight_fee'


class CbdRegionSeason(models.Model):
    season_id = models.AutoField(primary_key=True)
    region_id = models.IntegerField(unique=True)
    spring_start_time = models.IntegerField(blank=True, null=True)
    spring_end_time = models.IntegerField(blank=True, null=True)
    summer_start_time = models.IntegerField(blank=True, null=True)
    summer_end_time = models.IntegerField(blank=True, null=True)
    autumn_start_time = models.IntegerField(blank=True, null=True)
    autumn_end_time = models.IntegerField(blank=True, null=True)
    winter_start_time = models.IntegerField(blank=True, null=True)
    winter_end_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_region_season'


class CbdRequestErrorLog(models.Model):
    request_data = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    api = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cbd_request_error_log'


class CbdResembleFeedback(models.Model):
    user_id = models.BigIntegerField()
    goods_id = models.PositiveIntegerField()
    reason_id = models.PositiveIntegerField()
    reason_content = models.CharField(max_length=200)
    date = models.DateField()
    mobile = models.CharField(max_length=11)
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_resemble_feedback'


class CbdResembleFeedbackImage(models.Model):
    feedback_id = models.PositiveIntegerField()
    image_urll = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'cbd_resemble_feedback_image'


class CbdResembleFeedbackReason(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cbd_resemble_feedback_reason'


class CbdResourceLocation(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    resource_img = models.CharField(max_length=200, blank=True, null=True)
    target_type = models.IntegerField(blank=True, null=True)
    target = models.CharField(max_length=200, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)
    page_code = models.CharField(max_length=30)
    resource_channel_id = models.IntegerField()
    is_visible_app = models.IntegerField()
    is_visible_ouch_app = models.IntegerField()
    is_visible_dress_app = models.IntegerField()
    is_visible_xcx = models.IntegerField()
    is_visible_ouch_xcx = models.IntegerField()
    is_visible_dress_xcx = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_resource_location'


class CbdResourceLocationChannel(models.Model):
    type = models.IntegerField()
    create_time = models.IntegerField()
    last_create_uid = models.IntegerField()
    last_create_name = models.CharField(max_length=64)
    update_time = models.DateTimeField(blank=True, null=True)
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_resource_location_channel'


class CbdReturnApilog(models.Model):
    log_id = models.AutoField(primary_key=True)
    operate = models.CharField(max_length=20, blank=True, null=True)
    behavior = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    result = models.IntegerField(blank=True, null=True)
    order_id = models.IntegerField(blank=True, null=True)
    operator = models.CharField(max_length=20, blank=True, null=True)
    logtime = models.IntegerField()
    content_json = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_return_apilog'
        unique_together = (('log_id', 'logtime'),)


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
    only_refund = models.IntegerField()
    spec_name_one = models.CharField(max_length=40, blank=True, null=True)
    spec_name_two = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_return_goods'


class CbdReturnGoodsLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    return_no = models.CharField(max_length=50)
    erp_return_no = models.CharField(max_length=50)
    return_status = models.PositiveIntegerField()
    delivery_no = models.CharField(max_length=50)
    is_refuse = models.PositiveIntegerField()
    refuse_reason = models.CharField(max_length=500)
    is_cancel = models.PositiveIntegerField()
    source = models.CharField(max_length=50)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_return_goods_log'


class CbdReturnGoodsText(models.Model):
    batch_no = models.CharField(max_length=40)
    text_id = models.IntegerField()
    text = models.CharField(max_length=255)
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_return_goods_text'


class CbdReturnImg(models.Model):
    id = models.BigAutoField(primary_key=True)
    return_id = models.BigIntegerField()
    img_url = models.CharField(max_length=200)
    save_path = models.CharField(max_length=200)
    save_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cbd_return_img'


class CbdReturnNumLog(models.Model):
    od_id = models.BigIntegerField()
    return_num = models.IntegerField()
    remark = models.CharField(max_length=500)
    datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_return_num_log'


class CbdReturnReason(models.Model):
    return_reason = models.CharField(max_length=255)
    is_delete = models.IntegerField()
    is_default = models.PositiveIntegerField()
    must_txt = models.IntegerField()
    must_img = models.IntegerField()
    only_refund = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_return_reason'


class CbdRole(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    pid = models.SmallIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    ename = models.CharField(max_length=5, blank=True, null=True)
    create_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_role'


class CbdRoleUser(models.Model):
    role_id = models.PositiveIntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_role_user'


class CbdSaleMember(models.Model):
    sm_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    level = models.SmallIntegerField()
    effective_time = models.IntegerField()
    create_time = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=1)
    default_discount = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'cbd_sale_member'


class CbdScene(models.Model):
    id = models.IntegerField(blank=True, null=True)
    goods_scene = models.CharField(max_length=150, blank=True, null=True)
    scene_id = models.IntegerField(blank=True, null=True)
    scene_state = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_scene'


class CbdSearch(models.Model):
    search_id = models.AutoField(primary_key=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    search_content = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_search'


class CbdSecondKill(models.Model):
    kill_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    up_time = models.IntegerField(blank=True, null=True)
    down_time = models.IntegerField(blank=True, null=True)
    top_img = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_second_kill'


class CbdServiceDistribution(models.Model):
    service_name = models.CharField(max_length=255)
    config_param = models.CharField(max_length=255)
    ratio = models.IntegerField()
    service_type = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_service_distribution'


class CbdServiceDistributionLog(models.Model):
    user_id = models.IntegerField()
    user_login_id = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    data_json = models.CharField(max_length=255)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_service_distribution_log'


class CbdSetting(models.Model):
    key = models.CharField(unique=True, max_length=80)
    value = models.TextField()
    type = models.CharField(max_length=6)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_setting'


class CbdShareDoleCoupon(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_share_dole_coupon'


class CbdShareEvent(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    lastedit = models.TextField(blank=True, null=True)
    is_close = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_share_event'


class CbdShareList(models.Model):
    share_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    share = models.IntegerField(blank=True, null=True)
    share_time = models.IntegerField(blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_share_list'


class CbdShareTenDoleCoupon(models.Model):
    user_id = models.BigIntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_share_ten_dole_coupon'


class CbdShareToken(models.Model):
    st_id = models.AutoField(primary_key=True)
    order_id = models.BigIntegerField()
    order_no = models.CharField(max_length=40)
    user_id = models.BigIntegerField()
    token_num = models.PositiveIntegerField()
    left_num = models.PositiveIntegerField()
    use_num = models.IntegerField(blank=True, null=True)
    expire_time = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    is_send_notice = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_share_token'


class CbdShareTokenUser(models.Model):
    tu_id = models.AutoField(primary_key=True)
    st_id = models.IntegerField()
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    avatar = models.CharField(max_length=255)
    nickname = models.CharField(max_length=40)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.PositiveIntegerField()
    expire_time = models.PositiveIntegerField()
    is_rollback = models.IntegerField()
    s_user_id = models.BigIntegerField()
    s_order_id = models.BigIntegerField()
    s_avatar = models.CharField(max_length=255)
    s_nickname = models.CharField(max_length=40)
    s_amount = models.DecimalField(max_digits=10, decimal_places=2)
    dividing_formula = models.CharField(max_length=100, blank=True, null=True)
    is_send_notice = models.IntegerField(blank=True, null=True)
    token_num = models.PositiveIntegerField()
    b_s_order_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_share_token_user'


class CbdShareTokenUserLog(models.Model):
    tu_id = models.IntegerField()
    user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    dividing_formula = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.PositiveIntegerField()
    result = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_share_token_user_log'


class CbdShielding(models.Model):
    shield_id = models.AutoField(primary_key=True)
    shield_content = models.CharField(max_length=60, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    user_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_shielding'


class CbdShopCategory(models.Model):
    shop_cate_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)
    category_sort = models.IntegerField()
    tab_img = models.CharField(max_length=200, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    category_list = models.TextField(blank=True, null=True)
    show_state = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_shop_category'


class CbdShopFreightTemplate(models.Model):
    shop_id = models.IntegerField(blank=True, null=True)
    province = models.SmallIntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    incr_amount = models.DecimalField(max_digits=10, decimal_places=2)
    operator_time = models.IntegerField(blank=True, null=True)
    tpl_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_shop_freight_template'


class CbdShopSet(models.Model):
    brand_id = models.TextField(blank=True, null=True)
    goods_id = models.TextField(blank=True, null=True)
    gender = models.IntegerField()
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_shop_set'


class CbdSign(models.Model):
    user_id = models.BigIntegerField()
    amount = models.FloatField()
    inviter_id = models.BigIntegerField(blank=True, null=True)
    total_amount = models.FloatField()
    coupon_id = models.IntegerField(blank=True, null=True)
    add_time = models.IntegerField()
    type = models.IntegerField()
    is_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_sign'


class CbdSignQrImg(models.Model):
    user_id = models.BigIntegerField()
    qrimg = models.CharField(db_column='qrImg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    logoimg = models.CharField(db_column='logoImg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    shareimg = models.CharField(db_column='shareImg', max_length=100, blank=True, null=True)  # Field name made lowercase.
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_sign_qr_img'


class CbdSipCauseTianrun(models.Model):
    code = models.IntegerField(unique=True)
    message = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_sip_cause_tianrun'


class CbdSmsTemplate(models.Model):
    type = models.IntegerField()
    send_node = models.CharField(max_length=255)
    send_time_type = models.IntegerField()
    send_start_hour = models.IntegerField()
    send_end_hour = models.IntegerField()
    content = models.CharField(max_length=255)
    status = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_sms_template'


class CbdSpec(models.Model):
    spec_id = models.AutoField(primary_key=True)
    goods_id = models.IntegerField(blank=True, null=True)
    goods_no = models.CharField(max_length=100, blank=True, null=True)
    attr = models.TextField(blank=True, null=True)
    stocknum = models.IntegerField(blank=True, null=True)
    supply_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    crazy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    shop_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    flash_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    taojj_price = models.DecimalField(max_digits=10, decimal_places=2)
    vip_price = models.DecimalField(max_digits=10, decimal_places=2)
    group_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_putaway = models.IntegerField(blank=True, null=True)
    is_update = models.IntegerField(blank=True, null=True)
    is_defective = models.IntegerField(blank=True, null=True)
    ordernum = models.IntegerField(blank=True, null=True)
    buynum = models.IntegerField(blank=True, null=True)
    supplier_sku_no = models.CharField(max_length=100, blank=True, null=True)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    bak_crazy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    op_time = models.IntegerField(blank=True, null=True)
    buyamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    skusize = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    barcode = models.CharField(max_length=100, blank=True, null=True)
    is_sync = models.IntegerField(blank=True, null=True)
    random_num = models.IntegerField(blank=True, null=True)
    is_fbs_deleted = models.PositiveIntegerField()
    serial_number_code = models.CharField(max_length=255)
    update_time = models.IntegerField(blank=True, null=True)
    num_freeze = models.IntegerField()
    stock_warning = models.IntegerField(blank=True, null=True)
    stock_warning_num = models.IntegerField(blank=True, null=True)
    spec_name_one = models.CharField(max_length=40)
    spec_name_two = models.CharField(max_length=40)
    merchant_subsidy_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cbd_spec'


class CbdSpecStock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    goods_id = models.PositiveIntegerField()
    spec_id = models.PositiveIntegerField()
    shop_id = models.PositiveIntegerField()
    stocknum = models.IntegerField()
    ordernum = models.IntegerField()
    buynum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_spec_stock'
        unique_together = (('spec_id', 'shop_id'),)


class CbdSpecStockError(models.Model):
    spec_id = models.PositiveIntegerField()
    shop_id = models.PositiveIntegerField()
    stocknum = models.IntegerField()
    error_type = models.PositiveIntegerField()
    sql = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_spec_stock_error'


class CbdSpecial(models.Model):
    special_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    first_img = models.CharField(max_length=100, blank=True, null=True)
    banner_img = models.CharField(max_length=100, blank=True, null=True)
    show_goods = models.CharField(max_length=150)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    state = models.IntegerField(blank=True, null=True)
    is_visible_app = models.IntegerField(blank=True, null=True)
    is_visible_mini_program = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    last_editor = models.CharField(max_length=34, blank=True, null=True)
    last_edit_time = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special'


class CbdSpecialActivity(models.Model):
    special_id = models.IntegerField(blank=True, null=True)
    activity_start_time = models.IntegerField(blank=True, null=True)
    activity_end_time = models.IntegerField(blank=True, null=True)
    activity_label = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_activity'


class CbdSpecialChangebuyGoods(models.Model):
    changebuy_main_id = models.IntegerField()
    benefit_param = models.DecimalField(max_digits=10, decimal_places=2)
    changebuy_goods_ids = models.TextField()

    class Meta:
        managed = False
        db_table = 'cbd_special_changebuy_goods'


class CbdSpecialChangebuyMain(models.Model):
    changebuy_main_id = models.AutoField(primary_key=True)
    special_id = models.IntegerField()
    goods_ids = models.TextField()
    activity_kind = models.IntegerField()
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_special_changebuy_main'


class CbdSpecialClearTime(models.Model):
    special_id = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_clear_time'


class CbdSpecialCount(models.Model):
    count_id = models.AutoField(primary_key=True)
    special_id = models.IntegerField()
    clicknum = models.IntegerField(blank=True, null=True)
    salenum = models.IntegerField(blank=True, null=True)
    countdate = models.DateField()
    goodscount = models.IntegerField(blank=True, null=True)
    goodsnum = models.IntegerField(blank=True, null=True)
    average_goods_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    movesale = models.IntegerField(blank=True, null=True)
    shortsize = models.IntegerField(blank=True, null=True)
    shortsize_percent = models.IntegerField(blank=True, null=True)
    convertratio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    totalconvert = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supply_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    saleamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    supply_discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    crazy_coin = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)
    goods_collect = models.IntegerField(blank=True, null=True)
    male_option = models.IntegerField()
    female_option = models.IntegerField()
    uv = models.PositiveIntegerField()
    order_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_count'


class CbdSpecialDays(models.Model):
    yes_special_count = models.IntegerField(blank=True, null=True)
    yes_spec_count = models.IntegerField(blank=True, null=True)
    yes_sale_num = models.IntegerField(blank=True, null=True)
    yes_stock_num = models.IntegerField(blank=True, null=True)
    yes_sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    yes_stock_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tod_special_count = models.IntegerField(blank=True, null=True)
    tod_spec_count = models.IntegerField(blank=True, null=True)
    tod_sale_num = models.IntegerField(blank=True, null=True)
    tod_stock_num = models.IntegerField(blank=True, null=True)
    tod_sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tod_stock_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tom_special_count = models.IntegerField(blank=True, null=True)
    tom_spec_count = models.IntegerField(blank=True, null=True)
    tom_sale_num = models.IntegerField(blank=True, null=True)
    tom_stock_num = models.IntegerField(blank=True, null=True)
    tom_sale_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tom_stock_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_days'


class CbdSpecialGoods(models.Model):
    special_id = models.IntegerField()
    goods_id = models.IntegerField()
    goods_sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_goods'
        unique_together = (('special_id', 'goods_id'),)


class CbdSpecialGoodsDumpLog(models.Model):
    time = models.PositiveIntegerField()
    msg = models.TextField(blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_special_goods_dump_log'


class CbdSpecialOrder(models.Model):
    special_id = models.IntegerField(blank=True, null=True)
    schedule_date = models.DateField()
    schedule_time_point = models.IntegerField()
    ashang_index_sort = models.SmallIntegerField(blank=True, null=True)
    new_index_sort = models.SmallIntegerField(blank=True, null=True)
    index_sort = models.SmallIntegerField(blank=True, null=True)
    ashang_category_sort = models.SmallIntegerField(blank=True, null=True)
    new_category_sort = models.SmallIntegerField(blank=True, null=True)
    preheat_sort = models.SmallIntegerField(blank=True, null=True)
    category_sort = models.SmallIntegerField(blank=True, null=True)
    create_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()
    operator = models.IntegerField()
    index_sort_xcx = models.SmallIntegerField(blank=True, null=True)
    new_index_sort_xcx = models.SmallIntegerField(blank=True, null=True)
    preheat_sort_xcx = models.SmallIntegerField(blank=True, null=True)
    category_sort_xcx = models.SmallIntegerField(blank=True, null=True)
    new_category_sort_xcx = models.SmallIntegerField(blank=True, null=True)
    sort_ouch_app = models.SmallIntegerField(blank=True, null=True)
    index_sort_ouch_app = models.SmallIntegerField(blank=True, null=True)
    new_sort_ouch_app = models.SmallIntegerField(blank=True, null=True)
    new_index_sort_ouch_app = models.SmallIntegerField(blank=True, null=True)
    preheat_sort_ouch_app = models.SmallIntegerField(blank=True, null=True)
    sort_dress_app = models.SmallIntegerField(blank=True, null=True)
    index_sort_dress_app = models.SmallIntegerField(blank=True, null=True)
    new_sort_dress_app = models.SmallIntegerField(blank=True, null=True)
    new_index_sort_dress_app = models.SmallIntegerField(blank=True, null=True)
    preheat_sort_dress_app = models.SmallIntegerField(blank=True, null=True)
    sort_ouch = models.SmallIntegerField(blank=True, null=True)
    index_sort_ouch = models.SmallIntegerField(blank=True, null=True)
    new_sort_ouch = models.SmallIntegerField(blank=True, null=True)
    new_index_sort_ouch = models.SmallIntegerField(blank=True, null=True)
    preheat_sort_ouch = models.SmallIntegerField(blank=True, null=True)
    sort_dress = models.SmallIntegerField(blank=True, null=True)
    index_sort_dress = models.SmallIntegerField(blank=True, null=True)
    new_sort_dress = models.SmallIntegerField(blank=True, null=True)
    new_index_sort_dress = models.SmallIntegerField(blank=True, null=True)
    preheat_sort_dress = models.SmallIntegerField(blank=True, null=True)
    category_sort_ouch_app = models.SmallIntegerField(blank=True, null=True)
    new_category_sort_ouch_app = models.SmallIntegerField(blank=True, null=True)
    category_sort_dress_app = models.SmallIntegerField(blank=True, null=True)
    new_category_sort_dress_app = models.SmallIntegerField(blank=True, null=True)
    category_sort_ouch = models.SmallIntegerField(blank=True, null=True)
    new_category_sort_ouch = models.SmallIntegerField(blank=True, null=True)
    category_sort_dress = models.SmallIntegerField(blank=True, null=True)
    new_category_sort_dress = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_order'


class CbdSpecialOrderTag(models.Model):
    special_id = models.IntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    schedule_date = models.DateField()
    schedule_time_point = models.IntegerField()
    sort = models.SmallIntegerField(blank=True, null=True)
    create_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()
    operator = models.IntegerField()
    sort_xcx = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_order_tag'


class CbdSpecialParticular(models.Model):
    channel_id = models.AutoField(primary_key=True)
    special_id = models.IntegerField()
    channel_title = models.CharField(max_length=20)
    add_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_particular'


class CbdSpecialParticularGoods(models.Model):
    channel_id = models.IntegerField()
    goods_id = models.IntegerField()
    add_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_particular_goods'


class CbdSpecialPreviousCount(models.Model):
    special_id = models.IntegerField()
    return_pre_special_id = models.IntegerField()
    return_percent = models.FloatField()
    order_count = models.IntegerField()
    return_order_count = models.IntegerField()
    cancle_count = models.IntegerField()
    conversion_pre_special_id = models.IntegerField()
    conversion_percent = models.FloatField()
    sum_salenum = models.IntegerField()
    sum_clicknum = models.IntegerField()
    refresh_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_special_previous_count'


class CbdSpecialRemind(models.Model):
    special_id = models.IntegerField()
    user_id = models.BigIntegerField()
    remind_time = models.IntegerField()
    is_cancel = models.IntegerField()
    is_remind = models.IntegerField()
    jpush_msg_id = models.CharField(max_length=20)
    jpush_error_msg = models.CharField(max_length=255)
    jpush_error_code = models.IntegerField()
    push_time = models.PositiveIntegerField()
    app_resource = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_special_remind'


class CbdSpecialSortByTag(models.Model):
    sort_id = models.AutoField(primary_key=True)
    special_id = models.IntegerField()
    sort = models.SmallIntegerField(blank=True, null=True)
    tag_id = models.IntegerField(blank=True, null=True)
    is_auto = models.IntegerField(blank=True, null=True)
    sort_xcx = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_sort_by_tag'


class CbdSpecialTag(models.Model):
    category_key = models.CharField(max_length=30)
    tag_name = models.CharField(max_length=45)
    tag_key = models.CharField(max_length=40, blank=True, null=True)
    add_time = models.PositiveIntegerField()
    img_url = models.CharField(max_length=500, blank=True, null=True)
    img_size = models.CharField(max_length=15, blank=True, null=True)
    icon_url = models.CharField(max_length=500, blank=True, null=True)
    icon_pressed_url = models.CharField(max_length=500, blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    is_set = models.IntegerField(blank=True, null=True)
    alias_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_special_tag'


class CbdSpecialTagAssoc(models.Model):
    special_id = models.IntegerField()
    tag_id = models.PositiveIntegerField()
    category_key = models.CharField(max_length=30)
    tag_name = models.CharField(max_length=45)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_special_tag_assoc'


class CbdSpecialTagCategory(models.Model):
    category_key = models.CharField(unique=True, max_length=30)
    category_title = models.CharField(max_length=45, blank=True, null=True)
    weight = models.PositiveIntegerField()
    field_type = models.CharField(max_length=10)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_special_tag_category'


class CbdStocksInfo(models.Model):
    stock_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    create_date = models.CharField(unique=True, max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_stocks_info'


class CbdStyle(models.Model):
    style_id = models.AutoField(primary_key=True)
    style_name = models.CharField(max_length=60, blank=True, null=True)
    last_style_id = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_style'


class CbdStyleSpecial(models.Model):
    style_special_id = models.AutoField(primary_key=True)
    special_name = models.CharField(max_length=100)
    impose_sort = models.PositiveIntegerField()
    for_spring = models.IntegerField(blank=True, null=True)
    for_summer = models.IntegerField(blank=True, null=True)
    for_autumn = models.IntegerField(blank=True, null=True)
    for_winter = models.IntegerField(blank=True, null=True)
    sort = models.SmallIntegerField(blank=True, null=True)
    status = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    history_click = models.PositiveIntegerField()
    day_click = models.PositiveIntegerField()
    on_sale_time = models.IntegerField(blank=True, null=True)
    stop_sale_time = models.IntegerField(blank=True, null=True)
    is_delete = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_style_special'


class CbdStyleSpecialBrand(models.Model):
    union_id = models.AutoField(primary_key=True)
    style_special_id = models.IntegerField()
    brand_id = models.IntegerField()
    sort = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_style_special_brand'


class CbdStyleSpecialCategory(models.Model):
    union_id = models.AutoField(primary_key=True)
    style_special_id = models.IntegerField()
    brand_id = models.IntegerField()
    third_cate_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_style_special_category'


class CbdStyleSpecialDelete(models.Model):
    style_special_id = models.AutoField(primary_key=True)
    for_spring = models.IntegerField(blank=True, null=True)
    for_summer = models.IntegerField(blank=True, null=True)
    for_autumn = models.IntegerField(blank=True, null=True)
    for_winter = models.IntegerField(blank=True, null=True)
    impose_sort = models.IntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_style_special_delete'


class CbdSubKill(models.Model):
    kill_id = models.IntegerField(blank=True, null=True)
    goods_id = models.IntegerField(blank=True, null=True)
    crazy_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    init_sale_num = models.IntegerField(blank=True, null=True)
    special_id = models.IntegerField(blank=True, null=True)
    sort = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_sub_kill'


class CbdSupplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=200, blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    open_bank = models.CharField(max_length=200, blank=True, null=True)
    bank_no = models.CharField(max_length=40, blank=True, null=True)
    link_man = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    qq = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    receiver = models.CharField(max_length=100, blank=True, null=True)
    buyer = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    fbs_supplier_id = models.IntegerField(blank=True, null=True)
    holiday_settings = models.TextField(blank=True, null=True)
    qiyu_group_id = models.IntegerField()
    is_using = models.IntegerField()
    is_deleted = models.IntegerField()
    is_taojj = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_supplier'


class CbdSupplierBrand(models.Model):
    fbs_id = models.IntegerField()
    fbs_supplier_id = models.IntegerField()
    supplier_id = models.IntegerField()
    fbs_brand_id = models.IntegerField()
    brand_id = models.IntegerField()
    brand_type = models.IntegerField()
    service_qq = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    contact = models.CharField(max_length=30, blank=True, null=True)
    ext_number = models.CharField(max_length=30)
    add_time = models.PositiveIntegerField()
    is_using = models.IntegerField()
    display_in_xcx = models.IntegerField(blank=True, null=True)
    vip_discount = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    svip_discount = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    display_in_ouch = models.IntegerField(blank=True, null=True)
    display_in_ouch_xcx = models.IntegerField(blank=True, null=True)
    display_in_dress = models.IntegerField(blank=True, null=True)
    display_in_dress_xcx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_supplier_brand'


class CbdSupplierBrands(models.Model):
    supplier_brand_id = models.AutoField(primary_key=True)
    brand_id = models.IntegerField()
    supplier_id = models.IntegerField()
    add_time = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)
    brand_cachet = models.TextField(blank=True, null=True)
    show = models.IntegerField(blank=True, null=True)
    start_time = models.IntegerField(blank=True, null=True)
    end_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_supplier_brands'


class CbdSupplierCategoriesCertificate(models.Model):
    fbs_id = models.PositiveIntegerField()
    supplier_certificate_id = models.IntegerField()
    fbs_supplier_id = models.IntegerField()
    level_id = models.IntegerField()
    level_name = models.CharField(max_length=120)
    edit_type = models.IntegerField()
    is_domestic = models.IntegerField()
    is_import = models.IntegerField()
    is_self_marketing = models.IntegerField()
    goods_name = models.CharField(max_length=100)
    goods_url = models.CharField(max_length=255)
    goods_img_url = models.CharField(max_length=4000)
    audit_apply_time = models.IntegerField()
    audit_status = models.IntegerField()
    audit_uid_first = models.IntegerField()
    audit_name_first = models.CharField(max_length=64)
    audit_time_first = models.IntegerField()
    audit_uid_final = models.IntegerField()
    audit_name_final = models.CharField(max_length=64)
    audit_time_final = models.IntegerField()
    audit_failure_reason = models.CharField(max_length=255)
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    is_alert = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_supplier_categories_certificate'
        unique_together = (('fbs_supplier_id', 'level_id'),)


class CbdSupplierCategoriesCertificateImg(models.Model):
    fbs_id = models.PositiveIntegerField()
    categories_certificate_id = models.IntegerField()
    fbs_supplier_id = models.IntegerField()
    level_id = models.IntegerField()
    file_type = models.IntegerField()
    file_json = models.CharField(max_length=4000)
    isdel = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_supplier_categories_certificate_img'


class CbdSupplierCertificate(models.Model):
    fbs_id = models.PositiveIntegerField()
    fbs_supplier_id = models.IntegerField(unique=True)
    trademark = models.CharField(max_length=4000)
    other_info = models.CharField(max_length=4000)
    is_self_marketing = models.IntegerField()
    self_product = models.CharField(max_length=4000)
    self_marketing_farm = models.CharField(max_length=4000)
    self_marketing_handmade = models.CharField(max_length=4000)
    audit_apply_time = models.IntegerField()
    audit_status = models.IntegerField()
    audit_uid_first = models.IntegerField()
    audit_name_first = models.CharField(max_length=64)
    audit_time_first = models.IntegerField()
    audit_uid_final = models.IntegerField()
    audit_name_final = models.CharField(max_length=64)
    audit_time_final = models.IntegerField()
    audit_failure_reason = models.CharField(max_length=255)
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_supplier_certificate'


class CbdSupplierCopy(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=200, blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    open_bank = models.CharField(max_length=200, blank=True, null=True)
    bank_no = models.CharField(max_length=40, blank=True, null=True)
    link_man = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    qq = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    receiver = models.CharField(max_length=100, blank=True, null=True)
    buyer = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    fbs_supplier_id = models.IntegerField(blank=True, null=True)
    holiday_settings = models.TextField(blank=True, null=True)
    qiyu_group_id = models.IntegerField()
    is_using = models.IntegerField()
    is_deleted = models.IntegerField()
    is_taojj = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_supplier_copy'


class CbdSupplierCustomService(models.Model):
    supplier_id = models.PositiveIntegerField(unique=True)
    custom_service_id = models.CharField(unique=True, max_length=20)
    account = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    seat_number = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    operator = models.CharField(max_length=30)
    add_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_supplier_custom_service'


class CbdSupplierMarketing(models.Model):
    fbs_marketing_id = models.IntegerField(unique=True)
    marketing_name = models.CharField(max_length=100)
    supplier_id = models.IntegerField()
    fbs_supplier_id = models.IntegerField()
    marketing_type = models.IntegerField()
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    token_off = models.IntegerField()
    isdel = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_supplier_marketing'


class CbdSupplierMarketingGoods(models.Model):
    marketing_id = models.IntegerField()
    goods_id = models.IntegerField()
    isdel = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_supplier_marketing_goods'
        unique_together = (('marketing_id', 'goods_id'),)


class CbdSupplierMarketingLog(models.Model):
    sync_type = models.IntegerField(blank=True, null=True)
    sync_data = models.TextField(blank=True, null=True)
    sync_code = models.IntegerField(blank=True, null=True)
    msg = models.CharField(max_length=1000, blank=True, null=True)
    add_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_supplier_marketing_log'


class CbdSupplierMarketingType(models.Model):
    fbs_id = models.IntegerField(unique=True)
    marketing_id = models.IntegerField()
    coupon_amount = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_use_amount = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_num = models.IntegerField()
    use_coupon_num = models.IntegerField()
    fulloff_full_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fulloff_off_amount = models.DecimalField(max_digits=10, decimal_places=2)
    units_num = models.IntegerField()
    units_num_amount = models.DecimalField(max_digits=11, decimal_places=2)
    isdel = models.IntegerField()
    sync_to_fbs = models.IntegerField()
    coupon_draw_time = models.PositiveIntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_supplier_marketing_type'


class CbdSupplierQiyu(models.Model):
    supplier_id = models.IntegerField()
    group_id = models.IntegerField()
    group_name = models.CharField(max_length=30)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_supplier_qiyu'


class CbdSupplierQiyuAccount(models.Model):
    supplier_id = models.IntegerField(unique=True, blank=True, null=True)
    seat_number = models.IntegerField(blank=True, null=True)
    domain = models.CharField(max_length=50, blank=True, null=True)
    account = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    commercial_tenant_id = models.IntegerField(blank=True, null=True)
    update_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_supplier_qiyu_account'


class CbdSupplierQiyuKefu(models.Model):
    supplier_id = models.IntegerField()
    group_id = models.IntegerField()
    kefu_id = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    realname = models.CharField(max_length=20, blank=True, null=True)
    nickname = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    max_session = models.IntegerField(blank=True, null=True)
    add_time = models.PositiveIntegerField()
    update_time = models.IntegerField()
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_supplier_qiyu_kefu'


class CbdSupplierSaleCount(models.Model):
    count_date = models.DateField(blank=True, null=True)
    cate_name = models.CharField(max_length=50)
    supplier_name = models.CharField(max_length=255)
    supplier_id = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    sum_saleamount = models.DecimalField(max_digits=10, decimal_places=0)
    sum_salenum = models.IntegerField()
    refund_percent = models.CharField(max_length=10)
    bargain_amount = models.DecimalField(max_digits=10, decimal_places=0)
    bargain_num = models.IntegerField()
    discount_amount = models.DecimalField(max_digits=10, decimal_places=0)
    discount_num = models.IntegerField()
    secondkill_amount = models.DecimalField(max_digits=10, decimal_places=0)
    secondkill_num = models.IntegerField()
    newuser_amount = models.DecimalField(max_digits=10, decimal_places=0)
    newuser_num = models.IntegerField()
    shop_amount = models.DecimalField(max_digits=10, decimal_places=0)
    shop_num = models.IntegerField()
    special_click = models.IntegerField()
    specail_uv = models.IntegerField()
    special_num = models.IntegerField()
    special_order_count = models.IntegerField()
    special_amount = models.DecimalField(max_digits=10, decimal_places=0)
    special_click_return = models.CharField(max_length=10)
    special_uv_return = models.CharField(max_length=10)
    special_ticket_sale = models.DecimalField(max_digits=10, decimal_places=0)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_supplier_sale_count'


class CbdSwellRecord(models.Model):
    user_id = models.BigIntegerField()
    expansion_amount = models.DecimalField(max_digits=10, decimal_places=2)
    open_id = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    headimgurl = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=128, blank=True, null=True)
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_swell_record'


class CbdSystemlog(models.Model):
    log_id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=30, blank=True, null=True)
    module = models.CharField(max_length=40, blank=True, null=True)
    event = models.CharField(max_length=40, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    logtime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_systemlog'


class CbdTags(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30, blank=True, null=True)
    tag_img = models.CharField(max_length=200, blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tags'


class CbdTelCenterLog(models.Model):
    tcl_id = models.AutoField(primary_key=True)
    main_unique_id = models.CharField(max_length=255)
    customer_number = models.CharField(max_length=255)
    customer_area_code = models.CharField(max_length=255)
    customer_number_type = models.IntegerField()
    start_time = models.IntegerField()
    answer_time = models.IntegerField()
    join_queue_time = models.IntegerField()
    bridge_time = models.IntegerField()
    end_time = models.IntegerField()
    status = models.IntegerField()
    sip_cause_status = models.CharField(max_length=255)
    mark = models.IntegerField()
    number_trunk = models.CharField(max_length=255)
    bridged_cno = models.CharField(max_length=255)
    sip_cause = models.IntegerField()
    investigation_keys = models.CharField(max_length=255)
    investigation_start_time = models.IntegerField()
    investigation_end_time = models.IntegerField()
    is_get_sip_cause = models.PositiveIntegerField()
    is_get_investigation = models.PositiveIntegerField()
    create_time = models.IntegerField()
    number = models.CharField(max_length=255)
    bridgeduration = models.IntegerField(db_column='bridgeDuration')  # Field name made lowercase.
    result = models.IntegerField()
    transfernumber = models.CharField(db_column='transferNumber', max_length=255)  # Field name made lowercase.
    cdr_sip_cause = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tel_center_log'


class CbdTelCenterResult(models.Model):
    main_unique_id = models.CharField(unique=True, max_length=255)
    result = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tel_center_result'


class CbdTelCoupon(models.Model):
    tel = models.CharField(max_length=20)
    main_id = models.PositiveIntegerField()
    activity_id = models.IntegerField()
    coupon_name = models.CharField(max_length=50)
    type = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    undertaker_type = models.PositiveIntegerField()
    is_float_time = models.PositiveIntegerField()
    float_start_time = models.IntegerField()
    float_end_time = models.IntegerField()
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    is_get = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tel_coupon'


class CbdTelLog(models.Model):
    tl_id = models.AutoField(primary_key=True)
    main_unique_id = models.CharField(max_length=255)
    customer_number = models.CharField(max_length=255)
    customer_area_code = models.CharField(max_length=255)
    customer_number_type = models.IntegerField()
    start_time = models.IntegerField()
    answer_time = models.IntegerField()
    join_queue_time = models.IntegerField()
    bridge_time = models.IntegerField()
    end_time = models.IntegerField()
    status = models.IntegerField()
    sip_cause_status = models.CharField(max_length=255)
    mark = models.IntegerField()
    number_trunk = models.CharField(max_length=255)
    bridged_cno = models.CharField(max_length=255)
    sip_cause = models.IntegerField()
    investigation_keys = models.CharField(max_length=255)
    investigation_start_time = models.IntegerField()
    investigation_end_time = models.IntegerField()
    is_get_sip_cause = models.PositiveIntegerField()
    is_get_investigation = models.PositiveIntegerField()
    input = models.PositiveIntegerField()
    create_time = models.IntegerField()
    number = models.CharField(max_length=255)
    bridgeduration = models.IntegerField(db_column='bridgeDuration')  # Field name made lowercase.
    result = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tel_log'


class CbdTelLogError(models.Model):
    method = models.CharField(max_length=40)
    data = models.CharField(max_length=1000)
    error_log = models.CharField(max_length=255)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tel_log_error'


class CbdTelLogTask(models.Model):
    method = models.CharField(max_length=40)
    data = models.TextField()
    curl_error = models.CharField(max_length=255)
    curl_http_code = models.IntegerField()
    status = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tel_log_task'


class CbdTemplateCate(models.Model):
    union_tmp_id = models.IntegerField()
    cate_id = models.IntegerField()
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_template_cate'


class CbdTemplateClassifyImg(models.Model):
    union_tmp_id = models.IntegerField()
    img = models.CharField(max_length=200)
    img_op1 = models.CharField(max_length=200)
    img_op2 = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    target_type = models.IntegerField()
    target = models.CharField(max_length=200)
    width = models.IntegerField()
    height = models.IntegerField()
    img_op1_size = models.CharField(max_length=20)
    img_op2_size = models.CharField(max_length=20)
    img1 = models.CharField(max_length=200)
    countdown_bg_color = models.CharField(max_length=20)
    countdown_font_color = models.CharField(max_length=20)
    countdown_start_time = models.PositiveIntegerField()
    countdown_end_time = models.PositiveIntegerField()
    most_click_img_no = models.IntegerField()
    page_code = models.CharField(max_length=30)
    time_data_json = models.CharField(max_length=1000)
    time_data_json2 = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'cbd_template_classify_img'


class CbdTemplateImg(models.Model):
    union_tmp_id = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=200, blank=True, null=True)
    img_op1 = models.CharField(max_length=200, blank=True, null=True)
    img_op2 = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    target_type = models.IntegerField(blank=True, null=True)
    target = models.CharField(max_length=200, blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    img_op1_size = models.CharField(max_length=20, blank=True, null=True)
    img_op2_size = models.CharField(max_length=20, blank=True, null=True)
    img1 = models.CharField(max_length=200, blank=True, null=True)
    countdown_bg_color = models.CharField(max_length=20, blank=True, null=True)
    countdown_font_color = models.CharField(max_length=20, blank=True, null=True)
    countdown_start_time = models.PositiveIntegerField()
    countdown_end_time = models.PositiveIntegerField()
    most_click_img_no = models.IntegerField()
    page_code = models.CharField(max_length=30)
    time_data_json = models.TextField()
    time_data_json2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'cbd_template_img'


class CbdTemplateImgShop(models.Model):
    union_tmp_id = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    target_type = models.IntegerField(blank=True, null=True)
    target = models.CharField(max_length=200, blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    target1 = models.CharField(max_length=20, blank=True, null=True)
    target2 = models.CharField(max_length=20, blank=True, null=True)
    goods = models.TextField(blank=True, null=True)
    page_code = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cbd_template_img_shop'


class CbdTemplateImgTide(models.Model):
    union_tmp_id = models.IntegerField(blank=True, null=True)
    img = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    target_type = models.IntegerField(blank=True, null=True)
    target = models.CharField(max_length=200, blank=True, null=True)
    width = models.IntegerField()
    height = models.IntegerField()
    target1 = models.CharField(max_length=20, blank=True, null=True)
    target2 = models.CharField(max_length=20, blank=True, null=True)
    goods = models.TextField(blank=True, null=True)
    page_code = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cbd_template_img_tide'


class CbdTenGoods(models.Model):
    shop_id = models.PositiveIntegerField()
    goods_id = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_ten_goods'


class CbdTenShop(models.Model):
    shop_id = models.PositiveIntegerField()
    shop_name = models.CharField(max_length=50)
    shop_icon = models.CharField(max_length=100)
    shop_banner = models.CharField(max_length=200)
    goods_number = models.PositiveIntegerField()
    salves_number = models.PositiveIntegerField()
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    is_delete = models.PositiveIntegerField()
    is_show = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    supplier_id = models.PositiveIntegerField()
    home_goods = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'cbd_ten_shop'


class CbdTest(models.Model):
    bo_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    test = models.CharField(max_length=255, blank=True, null=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_test'


class CbdTgChannel(models.Model):
    channel = models.CharField(max_length=100, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tg_channel'


class CbdTgUser(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    account = models.CharField(unique=True, max_length=64)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    bind_account = models.CharField(max_length=50, blank=True, null=True)
    last_login_time = models.PositiveIntegerField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=40, blank=True, null=True)
    login_count = models.PositiveIntegerField(blank=True, null=True)
    verify = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    type_id = models.PositiveIntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tg_user'


class CbdTideBrand(models.Model):
    tide_id = models.AutoField(primary_key=True)
    brand_id = models.PositiveIntegerField()
    bg_img = models.CharField(max_length=300, blank=True, null=True)
    include_goods_categories = models.CharField(max_length=300, blank=True, null=True)
    create_time = models.PositiveIntegerField(blank=True, null=True)
    sales = models.PositiveIntegerField(blank=True, null=True)
    product_count = models.PositiveIntegerField()
    click_volume = models.PositiveIntegerField()
    return_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    popularity_sort = models.IntegerField()
    default_sort = models.IntegerField()
    is_delete = models.IntegerField(blank=True, null=True)
    thirty_sales = models.PositiveIntegerField()
    seven_sales = models.PositiveIntegerField()
    day_sales = models.PositiveIntegerField()
    day_diff = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'cbd_tide_brand'


class CbdTideBrandProperty(models.Model):
    bp_id = models.AutoField(primary_key=True)
    tide_id = models.IntegerField()
    brand_id = models.PositiveIntegerField()
    create_time = models.DateField()
    sales = models.PositiveIntegerField(blank=True, null=True)
    click_volume = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tide_brand_property'


class CbdTideCollectBrand(models.Model):
    brand_id = models.IntegerField()
    is_visible_sdj = models.IntegerField()
    is_visible_ouch = models.IntegerField()
    sort = models.SmallIntegerField()
    create_uid = models.IntegerField()
    create_name = models.CharField(max_length=64)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tide_collect_brand'


class CbdTideCollectGoods(models.Model):
    goods_id = models.IntegerField()
    is_visible_sdj = models.IntegerField()
    is_visible_ouch = models.IntegerField()
    sort = models.SmallIntegerField()
    create_uid = models.IntegerField()
    create_name = models.CharField(max_length=64)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tide_collect_goods'


class CbdTideHotsale(models.Model):
    goods_id = models.IntegerField()
    last_week_sale_count = models.IntegerField()
    last_online_time = models.IntegerField()
    last_offline_time = models.IntegerField()
    online_days_count = models.IntegerField()
    create_time = models.IntegerField()
    update_time = models.IntegerField()
    status = models.IntegerField()
    is_visible_app = models.IntegerField(blank=True, null=True)
    is_visible_ouch_app = models.IntegerField(blank=True, null=True)
    is_visible_dress_app = models.IntegerField(blank=True, null=True)
    is_visible_xcx = models.IntegerField(blank=True, null=True)
    is_visible_ouch = models.IntegerField(blank=True, null=True)
    is_visible_dress = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tide_hotsale'


class CbdTideHotsaleSort(models.Model):
    goods_id = models.IntegerField()
    sort = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tide_hotsale_sort'


class CbdTideHotsaleStat(models.Model):
    goods_id = models.PositiveIntegerField()
    date = models.DateField()
    click_times = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tide_hotsale_stat'
        unique_together = (('goods_id', 'date'),)


class CbdTideShop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=100)
    logo_url = models.CharField(max_length=200, blank=True, null=True)
    img_url = models.CharField(max_length=200, blank=True, null=True)
    supplier_id = models.IntegerField(blank=True, null=True)
    fbs_supplier_id = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    level_type = models.IntegerField(blank=True, null=True)
    level_sort = models.SmallIntegerField()
    is_recommend = models.IntegerField(blank=True, null=True)
    is_recommend_first = models.IntegerField(blank=True, null=True)
    recommend_first_sort = models.IntegerField(blank=True, null=True)
    is_recommend_second = models.IntegerField(blank=True, null=True)
    recommend_department = models.CharField(max_length=100, blank=True, null=True)
    recommend_second_sort = models.IntegerField(blank=True, null=True)
    is_tide = models.IntegerField(blank=True, null=True)
    tide_sort = models.SmallIntegerField()
    sort = models.SmallIntegerField()
    category_name = models.CharField(max_length=100, blank=True, null=True)
    main_name = models.CharField(max_length=100, blank=True, null=True)
    thirty_sales = models.PositiveIntegerField()
    goods_num = models.IntegerField(blank=True, null=True)
    week_top3_goods = models.CharField(max_length=50, blank=True, null=True)
    favorable_rate = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tide_shop'


class CbdTideShopBrand(models.Model):
    shop_id = models.IntegerField()
    brand_id = models.IntegerField()
    create_time = models.IntegerField(blank=True, null=True)
    is_delete = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tide_shop_brand'


class CbdTideShopSales(models.Model):
    shop_id = models.IntegerField()
    cat_id = models.IntegerField()
    goods_num = models.PositiveIntegerField()
    latest_month_sale = models.PositiveIntegerField()
    is_delete = models.IntegerField(blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tide_shop_sales'


class CbdTideSugoo(models.Model):
    title = models.CharField(max_length=50)
    cover_img = models.CharField(max_length=500)
    theme_style = models.IntegerField()
    url = models.CharField(max_length=500)
    status = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_tide_sugoo'


class CbdTideSugooChannel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    sugoo_id = models.IntegerField()
    channel_title = models.CharField(max_length=20)
    channel_img = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'cbd_tide_sugoo_channel'


class CbdTideSugooGoods(models.Model):
    channel_id = models.IntegerField()
    goods_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tide_sugoo_goods'


class CbdTideSugooStatistics(models.Model):
    sugoo_id = models.IntegerField()
    pv = models.IntegerField()
    sale = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_volume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cur_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    conversion_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tide_sugoo_statistics'


class CbdTideSugooStatisticsDay(models.Model):
    create_time = models.DateField()
    sugoo_id = models.IntegerField()
    pv = models.IntegerField()
    sale = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_volume = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tide_sugoo_statistics_day'


class CbdTjjshop(models.Model):
    user_id = models.BigIntegerField()
    shop_name = models.CharField(max_length=50, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    link_name = models.CharField(max_length=20, blank=True, null=True)
    link_phone = models.CharField(max_length=11, blank=True, null=True)
    link_email = models.CharField(max_length=50, blank=True, null=True)
    category_ids = models.CharField(max_length=50, blank=True, null=True)
    category_names = models.CharField(max_length=100, blank=True, null=True)
    shopkeeper_name = models.CharField(max_length=20, blank=True, null=True)
    certificates_id_type = models.IntegerField(blank=True, null=True)
    certificates_id = models.CharField(max_length=50, blank=True, null=True)
    certificates_type = models.IntegerField(blank=True, null=True)
    certificates_end_time = models.DateTimeField(blank=True, null=True)
    add_time = models.PositiveIntegerField(blank=True, null=True)
    update_time = models.PositiveIntegerField(blank=True, null=True)
    submit_time = models.PositiveIntegerField(blank=True, null=True)
    qq_number = models.BigIntegerField(blank=True, null=True)
    bd_mobile = models.CharField(max_length=11, blank=True, null=True)
    main_goods = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tjjshop'


class CbdTjjshopCompany(models.Model):
    info_id = models.IntegerField(blank=True, null=True)
    certificates_image_before = models.CharField(max_length=100, blank=True, null=True)
    certificates_image_after = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    company_province_id = models.IntegerField(blank=True, null=True)
    company_province_name = models.CharField(max_length=30, blank=True, null=True)
    company_city_id = models.IntegerField(blank=True, null=True)
    company_city_name = models.CharField(max_length=30, blank=True, null=True)
    company_district_id = models.IntegerField(blank=True, null=True)
    company_district_name = models.CharField(max_length=30, blank=True, null=True)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    credit_code = models.CharField(max_length=200, blank=True, null=True)
    company_image_business_licence = models.CharField(max_length=100, blank=True, null=True)
    company_image_account_opening_permit = models.CharField(max_length=100, blank=True, null=True)
    company_image_taxpayer_certificate = models.CharField(max_length=100, blank=True, null=True)
    company_trademark_json = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tjjshop_company'


class CbdTjjshopEnter(models.Model):
    mobile = models.CharField(max_length=11)
    type = models.PositiveIntegerField()
    create_time = models.DateTimeField()
    send_time = models.IntegerField()
    send_count = models.IntegerField()
    last_message = models.CharField(max_length=100)
    is_send = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tjjshop_enter'


class CbdTjjshopEnterImg(models.Model):
    info_id = models.IntegerField()
    image_url = models.CharField(max_length=100)
    img_no = models.IntegerField()
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()
    upload_result = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_tjjshop_enter_img'


class CbdTjjshopImgLog(models.Model):
    info_id = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    img_url = models.CharField(max_length=100)
    img_no = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    upload_result = models.IntegerField()
    is_delete = models.IntegerField(blank=True, null=True)
    is_used = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tjjshop_img_log'


class CbdTjjshopPerson(models.Model):
    info_id = models.IntegerField(blank=True, null=True)
    certificates_image_before = models.CharField(max_length=100, blank=True, null=True)
    certificates_image_after = models.CharField(max_length=100, blank=True, null=True)
    certificates_image_full = models.CharField(max_length=100, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tjjshop_person'


class CbdTmp20181224(models.Model):
    rownum = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'cbd_tmp_20181224'


class CbdToTransformOrder(models.Model):
    detail_no = models.CharField(unique=True, max_length=50)
    order_id = models.IntegerField()
    pay_time = models.IntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_to_transform_order'


class CbdTogether(models.Model):
    user_id = models.BigIntegerField()
    goods_id = models.IntegerField()
    spec_id = models.IntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    img = models.CharField(max_length=500, blank=True, null=True)
    size = models.CharField(max_length=20, blank=True, null=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    progress = models.IntegerField()
    create_time = models.IntegerField()
    order_id = models.IntegerField(blank=True, null=True)
    shop_id = models.IntegerField(blank=True, null=True)
    recover = models.IntegerField()
    re_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_together'


class CbdTranDetail(models.Model):
    tran_id = models.AutoField(primary_key=True)
    tran_time = models.CharField(max_length=30, blank=True, null=True)
    tran_context = models.TextField(blank=True, null=True)
    tran_updatestatus = models.CharField(max_length=30, blank=True, null=True)
    tran_areacode = models.CharField(max_length=20, blank=True, null=True)
    tran_areaname = models.CharField(max_length=30, blank=True, null=True)
    detail_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_tran_detail'


class CbdTransformCoin(models.Model):
    special_id = models.IntegerField()
    goods_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    crazy_coin = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_transform_coin'


class CbdU(models.Model):
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
        db_table = 'cbd_u'


class CbdUcl(models.Model):
    user_id = models.BigIntegerField()
    app_resource = models.IntegerField()
    source = models.CharField(max_length=50, blank=True, null=True)
    add_time = models.PositiveIntegerField()
    idfa = models.CharField(max_length=40)
    imei = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cbd_ucl'
        unique_together = (('user_id', 'app_resource'),)


class CbdUser(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    account = models.CharField(unique=True, max_length=64)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=32)
    phone = models.CharField(max_length=11, blank=True, null=True)
    bind_account = models.CharField(max_length=50, blank=True, null=True)
    last_login_time = models.PositiveIntegerField(blank=True, null=True)
    last_login_ip = models.CharField(max_length=40, blank=True, null=True)
    login_count = models.PositiveIntegerField(blank=True, null=True)
    verify = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.PositiveIntegerField()
    update_time = models.PositiveIntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    type_id = models.PositiveIntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    sms_verify = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_user'


class CbdUserActivityCount(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.BigIntegerField(unique=True)
    goods_cut_num = models.IntegerField()
    goods_boot_num = models.IntegerField()
    gold_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_activity_count'


class CbdUserActivityCoupon(models.Model):
    user_id = models.BigIntegerField()
    main_id = models.PositiveIntegerField()
    activity_id = models.IntegerField()
    coupon_name = models.CharField(max_length=50, blank=True, null=True)
    type = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    undertaker_type = models.PositiveIntegerField()
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()
    order_id = models.BigIntegerField()
    use_time = models.PositiveIntegerField()
    is_return_coupon = models.PositiveIntegerField()
    range = models.PositiveIntegerField()
    no_ceiling = models.PositiveIntegerField()
    is_read = models.IntegerField(blank=True, null=True)
    no_use_full_coupon = models.PositiveIntegerField()
    no_use_vip = models.PositiveIntegerField()
    fight_id = models.PositiveIntegerField()
    message_status = models.IntegerField()
    msg_unused = models.IntegerField()
    msg_coming_soon = models.IntegerField()
    store_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_activity_coupon'


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


class CbdUserBalance(models.Model):
    user_id = models.BigIntegerField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    actual_balance = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance = models.DecimalField(max_digits=10, decimal_places=2)
    frozen_balance = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_balance'


class CbdUserBalanceChangeLog(models.Model):
    user_id = models.BigIntegerField()
    src_user_id = models.BigIntegerField()
    order_id = models.BigIntegerField()
    detail_no = models.CharField(max_length=60)
    od_id = models.BigIntegerField()
    reason = models.CharField(max_length=21)
    balance_pre = models.DecimalField(max_digits=10, decimal_places=2)
    balance_change = models.DecimalField(max_digits=10, decimal_places=2)
    balance_post = models.DecimalField(max_digits=10, decimal_places=2)
    actual_balance_pre = models.DecimalField(max_digits=10, decimal_places=2)
    actual_balance_change = models.DecimalField(max_digits=10, decimal_places=2)
    actual_balance_post = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance_pre = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance_change = models.DecimalField(max_digits=10, decimal_places=2)
    available_balance_post = models.DecimalField(max_digits=10, decimal_places=2)
    frozen_balance_pre = models.DecimalField(max_digits=10, decimal_places=2)
    frozen_balance_change = models.DecimalField(max_digits=10, decimal_places=2)
    frozen_balance_post = models.DecimalField(max_digits=10, decimal_places=2)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_balance_change_log'


class CbdUserBalanceLog(models.Model):
    user_id = models.BigIntegerField()
    resource = models.CharField(max_length=22)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    post_balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_balance_log'


class CbdUserCategory(models.Model):
    uuid = models.CharField(max_length=100)
    user_id = models.BigIntegerField()
    cate_name = models.CharField(max_length=30)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_category'


class CbdUserChannelLog(models.Model):
    user_id = models.BigIntegerField()
    app_resource = models.IntegerField()
    source = models.CharField(max_length=50, blank=True, null=True)
    add_time = models.PositiveIntegerField()
    idfa = models.CharField(max_length=40)
    imei = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'cbd_user_channel_log'
        unique_together = (('user_id', 'app_resource'),)


class CbdUserCollectTideBrand(models.Model):
    user_id = models.BigIntegerField()
    brand_id = models.IntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_collect_tide_brand'
        unique_together = (('user_id', 'brand_id'),)


class CbdUserDataAnalysis(models.Model):
    user_id = models.BigIntegerField(unique=True)
    top_n_brand_id = models.CharField(max_length=100, blank=True, null=True)
    top_n_goods_id = models.TextField(blank=True, null=True)
    recent_n_brand_id = models.CharField(max_length=100, blank=True, null=True)
    add_time = models.PositiveIntegerField()
    last_update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_data_analysis'


class CbdUserDeviceTmp0818(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    click_time = models.CharField(max_length=19, blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    android_id = models.CharField(max_length=36, blank=True, null=True)
    imei = models.CharField(max_length=36, blank=True, null=True)
    uuid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_user_device_tmp_0818'


class CbdUserGlToken(models.Model):
    account = models.CharField(unique=True, max_length=30, blank=True, null=True)
    token = models.CharField(max_length=50, blank=True, null=True)
    update_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_user_gl_token'


class CbdUserGradeChangeLog(models.Model):
    user_id = models.BigIntegerField()
    reason = models.CharField(max_length=12)
    pre_grade = models.DecimalField(max_digits=2, decimal_places=1)
    change_grade = models.DecimalField(max_digits=2, decimal_places=1)
    order_id = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_grade_change_log'


class CbdUserInformation(models.Model):
    uuid = models.CharField(unique=True, max_length=100, blank=True, null=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    province_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    version = models.CharField(max_length=10, blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_information'


class CbdUserLikeBrand(models.Model):
    user_id = models.BigIntegerField()
    brand_id = models.PositiveIntegerField()
    push_status = models.PositiveIntegerField()
    push_remark = models.CharField(max_length=255)
    push_time = models.IntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_like_brand'
        unique_together = (('user_id', 'brand_id'),)


class CbdUserLoginLog(models.Model):
    account = models.CharField(max_length=30, blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    ip_country = models.CharField(max_length=10, blank=True, null=True)
    ip_area = models.CharField(max_length=10, blank=True, null=True)
    add_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_user_login_log'


class CbdUserMessage(models.Model):
    user_id = models.BigIntegerField()
    message_type = models.PositiveIntegerField()
    target_no = models.CharField(max_length=40)
    detail = models.CharField(max_length=2000)
    add_time = models.PositiveIntegerField()
    is_read = models.PositiveIntegerField()
    read_time = models.PositiveIntegerField()
    is_send = models.PositiveIntegerField()
    push_status = models.IntegerField()
    push_time = models.PositiveIntegerField()
    jpush_msg_id = models.CharField(max_length=20)
    jpush_error_msg = models.CharField(max_length=255)
    jpush_error_code = models.IntegerField()
    app_resource = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_message'


class CbdUserRecord(models.Model):
    user_id = models.BigIntegerField()
    create_time = models.PositiveIntegerField()
    log_type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_record'


class CbdUserRegDeviceInfo(models.Model):
    user_id = models.BigIntegerField()
    uuid = models.CharField(max_length=100)
    os = models.CharField(max_length=10)
    ifa = models.CharField(max_length=80)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_reg_device_info'


class CbdUserTagAssoc(models.Model):
    uuid = models.CharField(max_length=100)
    user_id = models.BigIntegerField()
    version = models.CharField(max_length=10, blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    tag_sign = models.CharField(max_length=45)
    access_ip = models.CharField(max_length=15, blank=True, null=True)
    app_resource = models.IntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_tag_assoc'


class CbdUserTagAssocDetail(models.Model):
    assoc_id = models.PositiveIntegerField()
    tag_id = models.PositiveIntegerField()
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_user_tag_assoc_detail'


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


class CbdUsersMarketing(models.Model):
    app_type = models.IntegerField(blank=True, null=True)
    user_id = models.BigIntegerField(unique=True, blank=True, null=True)
    first_order_time = models.IntegerField(blank=True, null=True)
    first_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    first_order_id = models.BigIntegerField(blank=True, null=True)
    last_order_time = models.IntegerField(blank=True, null=True)
    last_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    last_order_id = models.BigIntegerField(blank=True, null=True)
    total_order_num = models.IntegerField(blank=True, null=True)
    total_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_users_marketing'
        unique_together = (('app_type', 'user_id'),)


class CbdUsersMarketingTmp(models.Model):
    app_type = models.IntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    first_order_time = models.IntegerField(blank=True, null=True)
    first_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    first_order_id = models.IntegerField(blank=True, null=True)
    last_order_time = models.IntegerField(blank=True, null=True)
    last_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    last_order_id = models.IntegerField(blank=True, null=True)
    total_order_num = models.IntegerField(blank=True, null=True)
    total_order_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_users_marketing_tmp'
        unique_together = (('app_type', 'user_id'),)


class CbdUsersProfile(models.Model):
    user_id = models.BigIntegerField(unique=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    add_time = models.PositiveIntegerField()
    last_update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_users_profile'


class CbdUsersSignin(models.Model):
    user_id = models.BigIntegerField()
    is_vip = models.IntegerField()
    user_name = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    continuous_days = models.IntegerField()
    date = models.PositiveIntegerField(blank=True, null=True)
    type = models.IntegerField()
    parent_user_id = models.IntegerField()
    is_read = models.IntegerField(blank=True, null=True)
    create_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_users_signin'


class CbdUsersSigninfo(models.Model):
    user_id = models.BigIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_meet = models.IntegerField()
    update_time = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_users_signinfo'


class CbdUsersSource(models.Model):
    app_resource = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_users_source'


class CbdUserslog(models.Model):
    log_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    user_name = models.CharField(max_length=20, blank=True, null=True)
    mobile_id = models.CharField(max_length=20, blank=True, null=True)
    logintime = models.IntegerField(blank=True, null=True)
    os = models.CharField(max_length=10, blank=True, null=True)
    mobile_number = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_userslog'


class CbdUuidLog(models.Model):
    uuid = models.CharField(max_length=100)
    os = models.CharField(max_length=10)
    ifa = models.CharField(max_length=80, blank=True, null=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_uuid_log'


class CbdUvDay(models.Model):
    date = models.DateField()
    platform = models.IntegerField()
    uv = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_uv_day'
        unique_together = (('date', 'platform'),)


class CbdUvHour(models.Model):
    date = models.DateField()
    hour = models.IntegerField()
    platform = models.IntegerField()
    uv = models.IntegerField()
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_uv_hour'
        unique_together = (('date', 'hour', 'platform'),)


class CbdUvMinute(models.Model):
    date = models.DateField()
    time = models.TimeField()
    platform = models.IntegerField()
    uv = models.IntegerField()
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_uv_minute'
        unique_together = (('date', 'time', 'platform'),)


class CbdVersion(models.Model):
    type_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    now = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    new = models.CharField(max_length=15, blank=True, null=True)
    forced = models.CharField(max_length=30, blank=True, null=True)
    prompt = models.CharField(max_length=30, blank=True, null=True)
    silent = models.CharField(max_length=30, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    app_resource = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_version'


class CbdVersionSub(models.Model):
    type_id = models.IntegerField()
    prompt = models.CharField(max_length=30, blank=True, null=True)
    person = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_version_sub'


class CbdVipUser(models.Model):
    vip_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField()
    level = models.IntegerField()
    effective_time = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=1)
    create_time = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    is_temai = models.IntegerField()
    is_activity = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_vip_user'


class CbdVipUserCount(models.Model):
    count_date = models.DateField()
    vip_type = models.CharField(max_length=4)
    new_vip = models.IntegerField()
    payamount = models.DecimalField(max_digits=11, decimal_places=2)
    buy_count = models.IntegerField()
    total_buy_count = models.IntegerField()
    total_count = models.IntegerField()
    order_count = models.IntegerField()
    sale_amount = models.DecimalField(max_digits=11, decimal_places=2)
    kedan_price = models.IntegerField()
    maoli = models.CharField(max_length=10)
    total_order_count = models.IntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_vip_user_count'
        unique_together = (('vip_type', 'count_date'),)


class CbdVipUserOrder(models.Model):
    vu_id = models.AutoField(primary_key=True)
    order_no = models.CharField(max_length=40)
    user_id = models.BigIntegerField()
    amount = models.FloatField()
    level = models.SmallIntegerField()
    payment_id = models.IntegerField(blank=True, null=True)
    pay_state = models.PositiveIntegerField(blank=True, null=True)
    billno = models.CharField(max_length=60, blank=True, null=True)
    paytime = models.IntegerField(blank=True, null=True)
    payname = models.CharField(max_length=100, blank=True, null=True)
    payamount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    create_time = models.IntegerField()
    effective_time = models.PositiveIntegerField(blank=True, null=True)
    order_state = models.IntegerField()
    seller_id = models.CharField(max_length=50, blank=True, null=True)
    discount = models.DecimalField(max_digits=3, decimal_places=1)
    payno = models.CharField(max_length=60, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_vip_user_order'


class CbdVipUserOrderDuplicatePay(models.Model):
    order_id = models.IntegerField()
    order_no = models.CharField(max_length=50)
    billno = models.CharField(max_length=60)
    payamount = models.DecimalField(max_digits=10, decimal_places=2)
    paytime = models.IntegerField()
    paycode = models.CharField(max_length=50)
    payname = models.CharField(max_length=100)
    seller_id = models.CharField(max_length=50)
    add_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_vip_user_order_duplicate_pay'


class CbdVirtualHeadPortrait(models.Model):
    nickname = models.CharField(max_length=30)
    head_portrait = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cbd_virtual_head_portrait'


class CbdWithdrawCashLog(models.Model):
    base_number = models.FloatField(blank=True, null=True)
    rand_range = models.CharField(max_length=10, blank=True, null=True)
    real_range = models.CharField(max_length=10, blank=True, null=True)
    weight = models.CharField(max_length=1000, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_login_id = models.CharField(max_length=30, blank=True, null=True)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_withdraw_cash_log'


class CbdWithdrawCashSet(models.Model):
    base_number = models.FloatField(blank=True, null=True)
    rand_start = models.FloatField(blank=True, null=True)
    rand_end = models.FloatField(blank=True, null=True)
    weight = models.CharField(max_length=1000, blank=True, null=True)
    real_cash_start = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    real_cash_end = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_withdraw_cash_set'


class CbdWithdrawalsMobileLog(models.Model):
    user_id = models.BigIntegerField()
    action_log = models.TextField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_withdrawals_mobile_log'


class CbdWorldcupMatch(models.Model):
    number = models.IntegerField(blank=True, null=True)
    match_date = models.DateField(blank=True, null=True)
    match_time = models.CharField(max_length=10, blank=True, null=True)
    team_a = models.CharField(max_length=10, blank=True, null=True)
    team_b = models.CharField(max_length=10, blank=True, null=True)
    winner = models.CharField(max_length=10, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_worldcup_match'


class CbdWxUserAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    consignee = models.CharField(max_length=60, blank=True, null=True)
    province = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    district = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    mobile = models.CharField(max_length=15)
    best_time = models.CharField(max_length=120, blank=True, null=True)
    default = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cbd_wx_user_address'


class CbdWxUsers(models.Model):
    openid = models.CharField(unique=True, max_length=100)
    user_id = models.BigIntegerField(unique=True)
    add_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cbd_wx_users'


class CbdYearCateList(models.Model):
    cate_name = models.CharField(max_length=50)
    sort = models.PositiveIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_year_cate_list'


class CbdYearGoods(models.Model):
    cate_id = models.PositiveIntegerField()
    goods_id = models.PositiveIntegerField()
    goods_name = models.CharField(max_length=100)
    type = models.PositiveIntegerField()
    goods_sort = models.IntegerField()
    lottery_winner_num = models.PositiveIntegerField()
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cbd_year_goods'


class WdGoodsPunish(models.Model):
    goods_id = models.IntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wd_goods_punish'


class WdTjjThinkingWord(models.Model):
    original_name = models.CharField(max_length=200, blank=True, null=True)
    standard_name = models.CharField(max_length=200, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wd_tjj_thinking_word'


class WdWord(models.Model):
    original_name = models.CharField(max_length=120, blank=True, null=True)
    standard_name = models.CharField(max_length=120, blank=True, null=True)
    pinyin_all = models.CharField(max_length=120, blank=True, null=True)
    has_alias = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    word_type = models.IntegerField(blank=True, null=True)
    safe_level = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=20, blank=True, null=True)
    update_user = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wd_word'
