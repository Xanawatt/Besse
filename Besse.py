'''
 - Author: Mark Schneider (schne112@purdue.edu)	
 - Last Modified: 3/12/2021
 - Code to drive Besse the demo robot for PFP
 
 
 - TODO:
	- implement main loop
	- logging
		- for controller input implement a [Controller] event tag
	- actually drive the robot
	- have tuneable parameters from a web dashboard
		- things like motor speed, controller sensitivity, rumble, sound, cameras, etc.

'''

from evdev import InputDevice, ecodes, ff, list_devices

import gamepad # this is a third party library from here: 
import asyncio
debug = True

# Innitiate a connection to an xbox controller
def connect():
	xbox_path = None
	remote_control = None
	devices = [InputDevice(path) for path in list_devices()]
	print("[Besse] Connecting to Xbox controller...")
	for device in devices:
		if str.lower(device.name) == "xbox wireless controller":
			xbox_path = str(device.path)
			remote_control = gamepad.gamepad(file = xbox_path)
			remote_control.rumble_effect = 2
			print("[Besse] Connection successful")
			return remote_control
	return None

def drive():
	print("[Besse] Starting drive control...")
	# Play sound here for fun
	
	# While the controller is connected and the emergency stop button is not pressed
	while is_connected() and remote_control.button_b == False:
		# Drive the robot
		
		
	return

# copied function from here: https://github.com/erviveksoni/xbox-raspberrypi-rover/blob/bcea41f176bbf9dff62b48840f1a650cdca85b47/drive_rover.py#L189	
async def removetasks(loop):
    tasks = [t for t in asyncio.all_tasks() if t is not
             asyncio.current_task()]

    for task in tasks:
        # skipping over shielded coro still does not help
        if task._coro.__name__ == "cant_stop_me":
            continue
        task.cancel()

    print("Cancelling outstanding tasks")
    await asyncio.gather(*tasks, return_exceptions=True)
    loop.stop()	
	

	
if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	
	
	
	
	
	try:
		
		remote_control = connect()
		if remote_control == None:
			print("[Besse] Connection to Xbox controller has failed.")
			print("[Besse] Do you have the driver from here? https://github.com/atar-axis/xpadneo/tree/master/docs")
			
			
		# play initilization sound
		# delay for a set time
		# tasks = [third party libary method, rumble controller thread, drive thread]
		tasks = [remote_control.read_gamepad_imput(), remote_control.rumble(), drive()] # all of these are unimplemented dfunctions atm
		loop.run_until_complete(asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))
		# Nothing below this statement will run until execution is done or an error is thrown
		
		loop.run_until_complete(removetasks(loop))
		motor.destroy()
		# play disconnect sound
	
		
		
		
		
		
		
			
			
			
	except Exception as e:
		print("[Besse] An error has occurred: " + str(e)")
		# play error sound
		# delay
		print("[Besse] Shutting down...")
		# Play shutting down sound
		exit()

	finally:
		# if the remote_control ever connected
		if remote_control != None:
			remote_control.power_on = False # Turn off the controller
		
		print("[Besse] Shutting Down")
		loop.run_until_complete(loop.shutdown_asyncgens()) # Currently unimplemented function
		loop.close()
		
		GPIO.cleanup()
		print("Done")
		





