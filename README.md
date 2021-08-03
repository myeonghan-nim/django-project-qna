# Clone Project: QnA

## 1:N relation

```python
class Question(models.Model):
    title = models.CharField(max_length=200)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
```
