def light_curve(self, params):
		"""
		Calculate a model light curve.

		:param params: Transit parameters
		:type params: A `TransitParams` instance

		:return: Relative flux 
		:rtype: ndarray

		:Example:

		>>> flux = m.light_curve(params)
		"""
		#recalculates rsky and fac if necessary
		if params.t0 != self.t0 or params.per != self.per or params.a != self.a or params.inc != self.inc or params.ecc != self.ecc or params.w != self.w or params.t_secondary != self.t_secondary:
			if self.transittype == 2 and params.t_secondary != self.t_secondary:
				params.t0 = self.get_t_conjunction(params)
			self.ds= _rsky._rsky(self.t_supersample, params.t0, params.per, params.a, params.inc*pi/180., params.ecc, params.w*pi/180., self.transittype, self.nthreads)
		if params.limb_dark != self.limb_dark: self.fac = self._get_fac()

		#updates transit params
		self.t0 = params.t0
		self.per = params.per
		self.rp = params.rp
		self.a = params.a
		self.inc = params.inc
		self.ecc = params.ecc
		self.w = params.w
		self.u = params.u
		self.limb_dark = params.limb_dark
		self.fp = params.fp
		self.t_secondary = params.t_secondary
		self.inverse = False

		#handles the case of inverse transits (rp < 0)
		if self.rp < 0.: 
			self.rp = -1.*self.rp
			params.rp = -1.*params.rp
			self.inverse = True
		
		if self.transittype == 1:
			if params.limb_dark != self.limb_dark: raise Exception("Need to reinitialize model in order to change limb darkening option")
			if self.limb_dark == "quadratic": lc = _quadratic_ld._quadratic_ld(self.ds, params.rp, params.u[0], params.u[1], self.nthreads)
			elif self.limb_dark == "linear": lc = _quadratic_ld._quadratic_ld(self.ds, params.rp, params.u[0], 0., self.nthreads)
			elif self.limb_dark == "nonlinear": lc = _nonlinear_ld._nonlinear_ld(self.ds, params.rp, params.u[0], params.u[1], params.u[2], params.u[3], self.fac, self.nthreads)
			elif self.limb_dark == "squareroot": lc = _nonlinear_ld._nonlinear_ld(self.ds, params.rp, params.u[1], params.u[0], 0., 0., self.fac, self.nthreads)
			elif self.limb_dark == "uniform": lc = _uniform_ld._uniform_ld(self.ds, params.rp, self.nthreads)
			elif self.limb_dark == "logarithmic": lc = _logarithmic_ld._logarithmic_ld(self.ds, params.rp, params.u[0], params.u[1], self.fac, self.nthreads)
			elif self.limb_dark == "exponential": lc = _exponential_ld._exponential_ld(self.ds, params.rp, params.u[0], params.u[1], self.fac, self.nthreads)
			elif self.limb_dark == "power2": lc = _power2_ld._power2_ld(self.ds, params.rp, params.u[0], params.u[1], self.fac, self.nthreads)
			elif self.limb_dark == "custom": lc = _custom_ld._custom_ld(self.ds, params.rp, params.u[0], params.u[1], params.u[2], params.u[3], params.u[4], params.u[5], self.fac, self.nthreads)
			else: raise Exception("Invalid limb darkening option")

			if self.inverse == True: lc = 2. - lc

		else: lc = _eclipse._eclipse(self.ds, params.rp, params.fp, self.nthreads)			
		if self.supersample_factor == 1: return lc
		else: return np.mean(lc.reshape(-1, self.supersample_factor), axis=1)