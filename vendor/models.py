from django.db import models
from accounts.models import user, userProfile
from accounts.utils import vendorApproveStatus

# Create your models here.
class vendor(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE)
    userProfile = models.OneToOneField(userProfile, on_delete=models.CASCADE, blank=True, null=True)
    vendor_name = models.CharField(max_length=50, unique=True)
    vendor_licence = models.ImageField(upload_to="media/vendor/license/", blank=False, null=False)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.vendor_name
    
    def save(self, *args, **kwargs):
        if self.pk is not None:
            origin = vendor.objects.get(pk=self.pk)

            if self.is_approved != origin.is_approved:
                if self.is_approved == True:
                    messageSubject = "Congratulation ! your Resturant have been approved!"
                    vendorApproveStatus(messageSubject, self.is_approved, self.user)
                
                else:
                    messageSubject = "Resturant Profile Rejected"
                    vendorApproveStatus(messageSubject, self.is_approved, self.user)
        super(vendor, self).save(*args, **kwargs)
