# Django QnA

### QnA system with 1:N relation

```python
class Question(models.Model):

    # datas


class Answer(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
```