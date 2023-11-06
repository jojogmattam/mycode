#!/usr/bin/python3

rooms = {
            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : {
                      'key' : 'This key opens doors'
                  }
                },
            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : {
                      'monster' : 'A monster has appeared'
                  }
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'east' : 'Pantry',
                  'south': 'Garden',
                  'item' : {
                      'potion' : 'This potion has magical powers',
                      'crystal' : 'The crystal can get you teleported'
                  }
               },
            'Pantry' : {
                  'west' : 'Dining Room',
                  'item' : {
                      'card' : 'Thanks note saying "Thanks for playing"'
                  }
                  },
            'Garden' : {
                  'north' : 'Dining Room'
            }
         }

directions = ["south", "north", "east", "west"]
