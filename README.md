PyGame-Side-Collisions
======================

Custom `collided` functions for detect if sprites collided on a special side of another sprite.

##How it works

Simply add first a `velocity` attribute to the sprites, and set the `x` and `y` with their appropriates values. This property will bee useful for testing the collisions, and for add a speed to your sprite.

**But the `velocity` attribute doesn't give real speed to your sprite, you will need to update it yourself !**
See the code below:

```py
# A simple block class
class Block(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Create an image of the block, and fill it with a color.
        self.image = pygame.Surface([50, 20])
        self.image.fill([0,0,0])
        
        # Get rect & velocity
        self.rect = self.image.get_rect()
        self.velocity = side_collisions.Velocity()
        
        # Set dummy velocity
        self.velocity.x = 5
        self.velocity.y = 6
        
    # Update the position with velocity, that's you have to write
    def update(self):
        self.x = self.x+self.velocity.x
        self.y = self.y+self.velocity.y
```

##Docs

Not written yet.
See the [main file](https://github.com/DeathMiner/PyGame-Side-Collisions/blob/master/side_collisions.py) comments for info.

##License

Released under the [MIT License](https://github.com/DeathMiner/PyGame-Side-Collisions/blob/master/LICENSE)
