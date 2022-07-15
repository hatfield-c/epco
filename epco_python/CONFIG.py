import numpy as np

############################
#	ACTIONS
############################
action_playground = -1
action_train_save = 1
action_load_render = 2
action_train_render = 3
action_train_save_render = 4
action_train_video = 5
action_inference = 6

#action = action_train_video
#action = action_load_render
action = action_train_save
#action = action_playground

############################
#	PATHS
############################

train_path = "train.txt"

img_path = "render/model_space.png"
video_path = "render/frames/f"

model_save_path = "models/test"
model_load_path = "models/all-smooth-mid"

############################
#	HYPER PARAMETERS
############################

sizes = [ 2, 256, 256, 512, 512, 256, 256, 128, 64, 16, 8, 1 ]
#epochs = [ 200,  ]
epoch_list = [ 5, 5, 5 ]

batch_size = 128
epoch_size = 50
learning_rate = 1e-3
weight_decay = 1e-8

label_smooth = 1e-3

y_domain = [ -1, 8 ]
x_domain = [ -1, 11 ]

############################
#	MODEL PARAMETERS
############################

model_mode_separator = "SEPARATOR"
model_mode_smooth = "SMOOTH"

############################
#	TRAINING OUTPUT
############################

print_every_epoch = 20
print_every_batch = 25

############################
#	RENDER PARAMETERS
############################

render_debug = True

render_bot_threshold = 0
render_low_threshold = -25
render_mid_threshold = 0.5
render_high_threshold = 0.75
render_top_threshold = 1

#render_bot_threshold = -30
#render_low_threshold = -10
#render_mid_threshold = 0
#render_high_threshold = 8.55
#render_top_threshold = 8.8

render_bot_color = np.array((0, 0, 0))
render_low_color = np.array((0, 0, 255))
render_mid_color = np.array((255, 0, 0))
render_high_color = np.array((0, 255, 0))
render_top_color = np.array((255, 255, 255))

render_point_color = np.array((0, 255, 255))



y_width = y_domain[1] - y_domain[0]
x_width = x_domain[1] - x_domain[0]

img_scale = 18

img_size = [ int(y_width * img_scale), int(x_width * img_scale) ]
render_shape = np.array([ int(y_width * img_scale), int(x_width * img_scale), 3 ])

y_step = y_width / img_size[0]
x_step = x_width / img_size[1]

############################
#	TCP Parameters
############################

ip_addr = "localhost"
to_unity_port = '4044'
to_python_port = '4043'
tcp_buffer = 1024
tcp_timeout = 30