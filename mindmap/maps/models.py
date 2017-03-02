from django.db import models

class Map(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')#, related_name='maps')
    title = models.CharField(default='Untitled', max_length=100)
    # node = models.TextField(null=False)

    class Meta:
        ordering = ('created','title',)

    def __str__(self):
        return '%s - %s' % (self.title,self.created)

class Node(models.Model):
    map = models.ForeignKey(Map, related_name="nodes")
    type = models.CharField(default='Node', max_length=50)
    data = models.TextField(default='New Node', blank=True)

    def __str__(self):
        return self.data;
