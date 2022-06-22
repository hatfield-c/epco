
############################
#	PATHS
############################
train_path = "train.txt"

img_path = "render/model_space.png"


############################
#	HYPER PARAMETERS
############################
sizes = [ 2, 256, 256, 512, 512, 256, 256, 128, 64, 16, 8, 1 ]

epochs = 200
batch_size = 128
epoch_size = 50
learning_rate = 0.001

############################
#	TRAINING OUTPUT
############################

print_every_epoch = 20
print_every_batch = 25

############################
#	RENDER PARAMETERS
############################

y_domain = [ -1, 8 ]
x_domain = [ -1, 11 ]

y_width = y_domain[1] - y_domain[0]
x_width = x_domain[1] - x_domain[0]

img_scale = 18

img_size = [ int(y_width * img_scale), int(x_width * img_scale) ]

y_step = y_width / img_size[0]
x_step = x_width / img_size[1]

############################
#	TCP Parameters
############################

ip_addr = "localhost"
port = '7777'
tcp_buffer = 1024

#TCP_IP_ADDR = 'localhost'
#TCP_PORT_TO_UNITY = '4042'
#TCP_PORT_TO_SUMO = '4043'

#TCP_BUFFER = 1024