import numpy as np


def func(img,kernel,padding):
	channel = kernel.shape[0]
	k_size=  kernel.shape[1]
	height,width = img.shape[0],img.shape[1]
	if padding:
		img_pad = np.zeros((height+padding*2,width+padding*2))
		img_pad[padding:padding+height,padding:padding+width] = img
		img = img_pad
	out_img = np.zeros((channel,height+2*padding-k_size+1,width+2*padding-k_size+1))
	for i in range(channel):
		kernel_now = kernel[i]
		for step1 in range(width-k_size):
			for step2 in range(height-k_size):
				img_now = img[step2:step2+k_size,step1:step1+k_size]
				multi = img_now * kernel_now
				out_img[i,step1,step2] = np.sum(multi)
	return out_img


def conv(img,k_h,k_w,channel_out,padding):
	# img (B,C,H,W)
	batch,channel,height,weight = img.shape
	kernel = np.random.random((channel,channel_out,k_h,k_w))
	for b in range(batch):
		for ch in range(channel):
			img_c = img[b,ch,:,:]
			img_c_conv = func(img_c,kernel[ch,:,:,:],padding)
			img_c_conv = img_c_conv[np.newaxis,:]
			if ch==0:
				out_img = img_c_conv
			else:
				out_img = np.concatenate((out_img,img_c_conv))
		out_img = np.sum(out_img,axis=0)
		out_img = out_img[np.newaxis,:]
		if b==0:
			batch_out = out_img
		else:
			batch_out = np.concatenate((batch_out,out_img))
	return batch_out

img = np.random.random((2,3,15,15))
padding = conv(img,3,3,5,1).shape
origin = conv(img,3,3,5,0).shape
print(padding,origin)

