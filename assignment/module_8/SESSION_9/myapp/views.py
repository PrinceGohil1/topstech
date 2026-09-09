from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string


# =========================================================
# Home page — shows all 4 email forms
# URL: /
# =========================================================

def home(request):
    return render(request, "home.html")


# =========================================================
# Q1 — Test Email
# URL: /test-email/   POST: recipient_email
# =========================================================

def test_email(request):
    if request.method == "POST":
        recipient = request.POST.get("recipient_email", "").strip()
        try:
            send_mail(
                subject="Test Email from Django",
                message=(
                    "Hello!\n\n"
                    "This is a simple test email sent from Django "
                    "using Gmail SMTP.\n\n"
                    "If you received this, your email setup is working correctly.\n\n"
                    "Regards,\n"
                    "Django Dev Team"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=False,
            )
            return render(request, "home.html", {
                "message": f"✅ Test email sent successfully to {recipient}! Check your inbox."
            })
        except Exception as e:
            return render(request, "home.html", {
                "message": f"❌ Error sending email: {e}",
                "error": True,
            })
    return redirect("home")


# =========================================================
# Q2 — Password Reset Email
# URL: /send-reset-email/   POST: recipient_email
# =========================================================

def send_password_reset_email(request):
    if request.method == "POST":
        recipient = request.POST.get("recipient_email", "").strip()
        reset_link = f"http://127.0.0.1:8000/reset-password/?token=abc123xyz&email={recipient}"
        subject = "Reset Your Password – Action Required"
        message = f"""Hi there,

We received a request to reset the password for your account
associated with this email address: {recipient}

To reset your password, click the link below:

{reset_link}

This link is valid for the next 30 minutes only.

----------------------------------------------
Didn't request a password reset?
----------------------------------------------
If you did not make this request, you can safely ignore
this email. Your password will NOT be changed.

For security, please do not share this link with anyone.
Our support team will never ask for your password.

Need help? Contact us at support@mywebsite.com

Thanks,
The MyWebsite Security Team

--
© 2026 MyWebsite Pvt. Ltd. | All rights reserved
"""
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient],
                fail_silently=False,
            )
            return render(request, "home.html", {
                "message": f"✅ Password reset email sent to {recipient}!"
            })
        except Exception as e:
            return render(request, "home.html", {
                "message": f"❌ Error: {e}",
                "error": True,
            })
    return redirect("home")


# =========================================================
# Q3 + Q4 — Order Confirmation HTML Email
# URL: /order-email/   POST: recipient_email, user_name
# =========================================================

def send_order_confirmation(request):
    if request.method == "POST":
        recipient  = request.POST.get("recipient_email", "").strip()
        user_name  = request.POST.get("user_name", "Friend").strip()
        order_id   = "ORD-20260909-7842"

        items = [
            {"name": "Paneer Butter Masala", "quantity": 1, "price": 320},
            {"name": "Butter Naan",          "quantity": 3, "price": 90},
            {"name": "Veg Spring Rolls",     "quantity": 2, "price": 180},
            {"name": "Mango Lassi",          "quantity": 2, "price": 120},
        ]

        delivery_charge = 30
        subtotal = sum(item["price"] for item in items)
        total    = subtotal + delivery_charge

        context = {
            "user_name":       user_name,
            "order_id":        order_id,
            "items":           items,
            "subtotal":        subtotal,
            "delivery_charge": delivery_charge,
            "total":           total,
        }

        html_content = render_to_string("order_confirmation.html", context)

        items_text = "\n".join(
            f"  • {i['name']} × {i['quantity']}  =  ₹{i['price']}"
            for i in items
        )
        text_content = f"""Hello {user_name},

Your order has been successfully placed on FoodExpress! 🎉

Order ID : {order_id}
--------------------------------------------------
{items_text}
--------------------------------------------------
Subtotal        : ₹{subtotal}
Delivery Charge : ₹{delivery_charge}
Total Amount    : ₹{total}
--------------------------------------------------

Your delicious food is being prepared and will be delivered shortly. 🚀

Thank you for ordering with FoodExpress!

FoodExpress Delivery Team
support@foodexpress.in
"""
        try:
            email = EmailMultiAlternatives(
                subject="🎉 Order Confirmed! Your FoodExpress order is being prepared",
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            return render(request, "home.html", {
                "message": f"✅ Order confirmation email sent to {recipient}!"
            })
        except Exception as e:
            return render(request, "home.html", {
                "message": f"❌ Error: {e}",
                "error": True,
            })
    return redirect("home")


# =========================================================
# Q5 — IPL Fantasy League Welcome Email
# URL: /ipl-email/   POST: recipient_email
# =========================================================

def send_ipl_welcome_email(request):
    if request.method == "POST":
        recipient = request.POST.get("recipient_email", "").strip()

        subject = "🏏 Welcome to IPL Fantasy League – Your Dream Team Awaits!"

        text_content = """Welcome to IPL Fantasy League! 🏏

Hey Cricket Champion,

You just made the best decision of your cricket season.
Welcome aboard IPL Fantasy League — where every boundary,
wicket, and six earns YOU points!

🔥 HERE'S WHAT YOU CAN DO:
  • Build your Dream XI from 200+ IPL players
  • Set your captain & vice-captain for 2× & 1.5× points
  • Join public & private contests with your friends
  • Win exciting prizes every match day

🏆 YOUR FIRST CHALLENGE:
  Log in now and create your first team before today's match.
  Early birds always have an edge!

💡 PRO TIP:
  Keep an eye on the Playing XI announcements 30 minutes
  before the toss — that's when the real game begins!

Let the fantasy battle begin. May your team top the leaderboard!

Good luck! 🍀

– The IPL Fantasy League Team
support@iplfantasy.in
"""

        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to IPL Fantasy League</title>
</head>
<body style="margin:0;padding:0;background-color:#0a0a1a;font-family:Arial,sans-serif;">
<table width="100%" cellpadding="0" cellspacing="0" style="background-color:#0a0a1a;padding:30px 0;">
<tr><td align="center">
<table width="600" cellpadding="0" cellspacing="0"
       style="background-color:#111133;border-radius:16px;overflow:hidden;max-width:600px;">

    <!-- Header -->
    <tr>
        <td style="background:linear-gradient(135deg,#1a1aff,#ff6600);padding:40px 30px;text-align:center;">
            <h1 style="color:#fff;margin:0;font-size:32px;">🏏 IPL Fantasy League</h1>
            <p style="color:#ffe0b2;margin:10px 0 0;font-size:16px;">Where Every Run Counts</p>
        </td>
    </tr>

    <!-- Welcome -->
    <tr>
        <td style="padding:35px 40px;color:#e0e0e0;">
            <h2 style="color:#ff6600;margin-top:0;">Hey Cricket Champion! 👋</h2>
            <p style="font-size:16px;line-height:1.7;">
                You just joined the most exciting cricket fantasy platform of the season.
                Build your <strong style="color:#fff;">Dream XI</strong>, outsmart your rivals,
                and climb to the top of the leaderboard!
            </p>
        </td>
    </tr>

    <!-- Feature grid -->
    <tr>
        <td style="padding:0 40px 30px;">
            <table width="100%" cellpadding="0" cellspacing="0">
                <tr>
                    <td width="48%" style="background:#1a1a3e;border-radius:10px;padding:20px;vertical-align:top;">
                        <div style="font-size:28px;">🎯</div>
                        <h4 style="color:#ff6600;margin:10px 0 6px;">Pick Your XI</h4>
                        <p style="color:#aaa;font-size:13px;margin:0;">Choose from 200+ IPL superstars and form your perfect squad.</p>
                    </td>
                    <td width="4%"></td>
                    <td width="48%" style="background:#1a1a3e;border-radius:10px;padding:20px;vertical-align:top;">
                        <div style="font-size:28px;">⚡</div>
                        <h4 style="color:#ff6600;margin:10px 0 6px;">Earn Points Live</h4>
                        <p style="color:#aaa;font-size:13px;margin:0;">Watch your score update in real-time as the match unfolds.</p>
                    </td>
                </tr>
                <tr><td colspan="3" style="height:16px;"></td></tr>
                <tr>
                    <td width="48%" style="background:#1a1a3e;border-radius:10px;padding:20px;vertical-align:top;">
                        <div style="font-size:28px;">🏆</div>
                        <h4 style="color:#ff6600;margin:10px 0 6px;">Win Prizes</h4>
                        <p style="color:#aaa;font-size:13px;margin:0;">Compete in contests and win exciting rewards every match day.</p>
                    </td>
                    <td width="4%"></td>
                    <td width="48%" style="background:#1a1a3e;border-radius:10px;padding:20px;vertical-align:top;">
                        <div style="font-size:28px;">👥</div>
                        <h4 style="color:#ff6600;margin:10px 0 6px;">Challenge Friends</h4>
                        <p style="color:#aaa;font-size:13px;margin:0;">Create private leagues and battle your friends all season long.</p>
                    </td>
                </tr>
            </table>
        </td>
    </tr>

    <!-- Pro tip -->
    <tr>
        <td style="padding:0 40px 30px;">
            <div style="background:#2a1a00;border-left:4px solid #ff6600;border-radius:8px;padding:18px 20px;">
                <p style="color:#ffcc80;margin:0;font-size:14px;">
                    <strong>💡 Pro Tip:</strong> Check the Playing XI announcement
                    30 minutes before the toss — that's your edge over the competition!
                </p>
            </div>
        </td>
    </tr>

    <!-- CTA -->
    <tr>
        <td style="padding:0 40px 40px;text-align:center;">
            <a href="http://127.0.0.1:8000/"
               style="display:inline-block;background:linear-gradient(135deg,#ff6600,#ff3300);
                      color:#fff;text-decoration:none;padding:16px 48px;border-radius:50px;
                      font-size:18px;font-weight:bold;">
                🏏 Build My Dream Team
            </a>
        </td>
    </tr>

    <!-- Footer -->
    <tr>
        <td style="background:#0a0a1a;padding:25px 40px;text-align:center;border-top:1px solid #222244;">
            <p style="color:#555;font-size:12px;margin:0;">
                © 2026 IPL Fantasy League · All rights reserved<br>
                <a href="#" style="color:#555;">Unsubscribe</a> ·
                <a href="#" style="color:#555;">Privacy Policy</a>
            </p>
        </td>
    </tr>

</table>
</td></tr>
</table>
</body>
</html>"""

        try:
            email = EmailMultiAlternatives(
                subject=subject,
                body=text_content,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient],
            )
            email.attach_alternative(html_content, "text/html")
            email.send()
            return render(request, "home.html", {
                "message": f"✅ IPL Fantasy welcome email sent to {recipient}!"
            })
        except Exception as e:
            return render(request, "home.html", {
                "message": f"❌ Error: {e}",
                "error": True,
            })
    return redirect("home")
