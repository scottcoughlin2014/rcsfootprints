from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Create your models here.
class Issue(models.Model):
    """Model that defines metadata about a product

        :param product_name: Name of product being sold.
        :type product_name: str

        :param description: Description of product being sold.
        :type description: str
    """
    user_email = models.EmailField()
    fp_ticket_number = models.IntegerField()
    fp_ticket_title = models.CharField(max_length =400)
    fp_ticket_description = RichTextField()
    fp_ticket_thread_id = models.CharField(max_length =400)


    PYTHON = 'Python'
    SLURM = 'Slurm'
    NONE = None
    TOPIC_CHOICES = [
        (NONE, None),
        (SLURM, 'Slurm'),
    ]

    fp_tickets_topic = models.CharField(
        max_length=15,
        choices=TOPIC_CHOICES,
        default=NONE,
    )
    fp_tickets_autoresponse = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
