from ..config.settings import SPACE_GRAVITY, SPACE_FRICTION, BOUNCE_FACTOR, TILE_SIZE, MAX_SPEED  # Add MAX_SPEED import

class PhysicsManager:
    def __init__(self):
        self.gravity = SPACE_GRAVITY

    def apply_space_physics(self, entity):
        # Apply space friction
        entity.velocity.x *= SPACE_FRICTION
        entity.velocity.y *= SPACE_FRICTION
        
        # Apply gravity
        entity.velocity.y += self.gravity
        
        # Ensure no rotation is applied
        entity.rotation = 0
        
        # Limit velocity
        self._limit_velocity(entity)
        
        return entity.velocity

    def check_collision(self, entity, world):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        dx = entity.velocity.x
        dy = entity.velocity.y

        # Check x direction collision
        entity.rect.x += dx
        for tile in world.obstacle_list:
            if tile[1].colliderect(entity.rect):
                if dx > 0:  # Moving right
                    entity.rect.right = tile[1].left
                    collision_types['right'] = True
                elif dx < 0:  # Moving left
                    entity.rect.left = tile[1].right
                    collision_types['left'] = True
                dx = 0

        # Check y direction collision
        entity.rect.y += dy
        for tile in world.obstacle_list:
            if tile[1].colliderect(entity.rect):
                if dy > 0:  # Falling down
                    entity.rect.bottom = tile[1].top
                    collision_types['bottom'] = True
                    entity.in_air = False
                elif dy < 0:  # Jumping up
                    entity.rect.top = tile[1].bottom
                    collision_types['top'] = True
                dy = 0

        # Update entity velocity
        entity.velocity.x = dx
        entity.velocity.y = dy

        return collision_types

    def _limit_velocity(self, entity):
        # Limit maximum velocity
        max_speed = entity.max_speed if hasattr(entity, 'max_speed') else MAX_SPEED
        speed = (entity.velocity.x ** 2 + entity.velocity.y ** 2) ** 0.5
        if speed > max_speed:
            factor = max_speed / speed
            entity.velocity.x *= factor
            entity.velocity.y *= factor
