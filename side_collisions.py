#   # # # #        _____ _     __        ______      _____      _                 
#   # # # #? ?    / ___/(_)___/ /__     / ____/___  / / (_)____(_)___  ____  _____
#   # # # #? ?    \__ \/ / __  / _ \   / /   / __ \/ / / / ___/ / __ \/ __ \/ ___/
#   # # # #? ?   ___/ / / /_/ /  __/  / /___/ /_/ / / / (__  ) / /_/ / / / (__  ) 
#      ? ? ? ?  /____/_/\__,_/\___/   \____/\____/_/_/_/____/_/\____/_/ /_/____/  
#
# Checks collisions on wich side of sprite
# v0.0.1
# By Death_Miner
# MIT License

import pygame

#
# Sets velocity properties for a sprite
# 
# @class Velocity
class Velocity():

	#
	# Instantiates the class
	# 
	# @param object self     The class itself
	# @param list   velocity The velocity to apply, default is 0 on both axis
	# @return void
	def __init__(self, velocity=[0,0]):

		#
		# Velocity in x axis
		# 
		# @var int
		self.x = velocity[0]
	
		#
		# Velocity in x axis
		# 
		# @var int
		self.y = velocity[1]

#
# Check if B collide on left of A
# 
# @param object A The First sprite to check collision to
# @param object B The second sprite wich would collide A on left
def left(A, B):

	# Set velocity to B if there's no
	if hasattr(B, "velocity") == False:
		B.velocity = Velocity()

	# First check if A & B collide themselves
	if pygame.sprite.collide_rect(A, B) == True:
		
		# Check if right points of B are in A
		if A.rect.collidepoint(B.rect.midright) == True and (\
		   A.rect.collidepoint(B.rect.topright) == True or \
		   A.rect.collidepoint(B.rect.bottomright) == True):

		    # Check if B velocity moves to the left
			if B.velocity.x > 0:
				return True

	# Instead return False	
	return False

#
# Check if B collide on right of A
# 
# @param object A The First sprite to check collision to
# @param object B The second sprite wich would collide A on right
def right(A, B):

	# Set velocity to B if there's no
	if hasattr(B, "velocity") == False:
		B.velocity = Velocity()

	# First check if A & B collide themselves
	if pygame.sprite.collide_rect(A, B) == True:
		
		# Check if left points of B are in A
		if A.rect.collidepoint(B.rect.midleft) == True and (\
		   A.rect.collidepoint(B.rect.topleft) == True or \
		   A.rect.collidepoint(B.rect.bottomleft) == True):

		    # Check if B velocity moves to the right
			if B.velocity.x < 0:
				return True

	# Instead return False	
	return False

#
# Check if B collide on top of A
# 
# @param object A The First sprite to check collision to
# @param object B The second sprite wich would collide A on top
def top(A, B):

	# Set velocity to B if there's no
	if hasattr(B, "velocity") == False:
		B.velocity = Velocity()

	# First check if A & B collide themselves
	if pygame.sprite.collide_rect(A, B) == True:
		
		# Check if bottom points of B are in A
		if A.rect.collidepoint(B.rect.midbottom) == True and (\
		   A.rect.collidepoint(B.rect.bottomleft) == True or \
		   A.rect.collidepoint(B.rect.bottomright) == True):

		    # Check if B velocity moves to the top
			if B.velocity.y < 0:
				return True

	# Instead return False	
	return False

#
# Check if B collide on bottom of A
# 
# @param object A The First sprite to check collision to
# @param object B The second sprite wich would collide A on bottom
def bottom(A, B):

	# Set velocity to B if there's no
	if hasattr(B, "velocity") == False:
		B.velocity = Velocity()

	# First check if A & B collide themselves
	if pygame.sprite.collide_rect(A, B) == True:
		
		# Check if top points of B are in A
		if A.rect.collidepoint(B.rect.midtop) == True and (\
		   A.rect.collidepoint(B.rect.topleft) == True or \
		   A.rect.collidepoint(B.rect.topright) == True):

		    # Check if B velocity moves to the bottom
			if B.velocity.y < 0:
				return True

	# Instead return False	
	return False

#
# Sets multiple side detection
#
class __Multiple():
	
	#
	# Inits __Multiple class
	#
	# @param object self  The class itself
	# @param list   sides The sides wich has to be detected
	def __init__(self, sides):
		self.sides = sides
	
	#
	# Checks detection on multiple sides
	#
	# @param object self The class itself
	# @param object A    The first sprite
	# @param object B    The second sprite
	def fcn(self, A, B):
		
		# Navigate trough list
		for side in sef.sides:
			
			# Check for left if selected
			if side == "left":
				if left(A, B) == True:
					return True
					
			# Check for right if selected
			elif side == "right":
				if right(A, B) == True:
					return True
					
			# Check for top if selected
			elif side == "top":
				if top(A, B) == True:
					return True
					
			# Check for bottom if selected
			elif side == "bottom":
				if bottom(A, B) == True:
					return True
			
			# Error if invalid side name
			else:
				print("Unknown side name passed in multiple side detections: \""+str(side)+"\"")
				
		# Return False if no collision detected
		return False

#
# Check for collisions on multiple sides
#
# @param list A list of collisions: left, right, top, bottom available
def multiple(sides):
	return __Multiple(sides).fcn
	
