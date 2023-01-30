import stripe

def check_coupon(coupon_code):
  stripe.api_key = "sk_test_51KbgkpSDtFmq7yIYzw8zNwiG6Pl13RuwYyMeQ506l7Fw9Jgd2QM9qz50NzAe9s4AFXCVJm6azuPqK4Ta0RJUEgNu00v6U8xFyz"

  coupon = stripe.Coupon.retrieve(coupon_code)
  if coupon:
    return True
  else: 
    return False