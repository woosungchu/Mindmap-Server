from django.db import models

class Map(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')#, related_name='maps')
    title = models.CharField(default='Untitled', max_length=100)

    class Meta:
        ordering = ('created','title',)

    def __str__(self):
        return '%s. %s' % (self.id,self.title)

class Node(models.Model):
    NODE_TYPE = (('N','Node'),('T','Textbox'),)
    map = models.ForeignKey(Map, related_name="nodes", on_delete=models.CASCADE)
    type = models.CharField(default='N', max_length=50, choices=NODE_TYPE)
    content = models.TextField(default='New Node', blank=True)

    def __str__(self):
        content = (self.content[:75] + '..') if len(self.content) > 75 else self.content
        return '%s.%s - %s.%s' % (self.map.id, self.map.title, self.id, content)
