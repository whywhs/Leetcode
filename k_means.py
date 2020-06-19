import numpy as np


class k_means(object):
	def __init__(self,max_iter=10000,tolerance=0.0001,k=2):
		self.k = k
		self.max_iter = max_iter
		self.tolerance = tolerance

	def fit(self,data):
		self.center = {}
		for i in range(self.k):
			self.center[i] = data[i]

		for i in range(self.max_iter):
			self.cls = {i:[] for i in range(self.k)}

			for fea in data:
				distance = [np.linalg.norm(fea-self.center[cen]) for cen in self.center]
				class_now = distance.index(min(distance))
				self.cls[class_now].append(fea)

			optim = True
			for c in self.cls:
				c_now = np.average(self.cls[c],axis=0)
				c_pre = self.center[c]
				loss = np.sum((c_now-c_pre)/c_pre)
				if loss>self.tolerance:
					optim = False
				self.center[c] = c_now

			if optim: break

	def predict(self,p_data):
		cls_p = {i:[] for i in range(self.k)}
		for fea_p in p_data:
			distance = [np.linalg.norm(fea_p-self.center[cen]) for cen in self.center]
			idx = distance.index(min(distance))
			cls_p[idx].append(fea_p)
		return cls_p





