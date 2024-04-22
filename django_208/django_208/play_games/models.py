from django.db import models

# Create your models here.
from django.db import models
from medic_platform.models import Game


# class Game(models.Model):
#     # 假设你已经有一个Game模型
#     # ...
#     pass

class GameSpecification(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='specifications')
    save_hash = models.CharField(max_length=255)
    play_duration = models.IntegerField(help_text="Duration of a single game play in seconds.")
    start_time = models.DateTimeField(help_text="When the game play started.")

    class Meta:
        verbose_name = "Game Specification"
        verbose_name_plural = "Game Specifications"

    def __str__(self):
        return f"Specifications for {self.game.game_name}"
