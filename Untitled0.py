
# coding: utf-8

# In[1]:

pylab inline


# In[2]:

import matplotlib.pyplot as plt


# In[3]:

plt.plot(np.random.rand(100))


# In[1]:

y2 = np.sin(x**2)
plt.plot(x, y, label=r'$\sin(x)$')
plt.plot(x, y2, label=r'$\sin(x^2)$')
plt.title('Some functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend();


# In[2]:

get_ipython().magic(u'pylab inline')
import matplotlib.pyplot as plt


# In[3]:

plt.plot(np.random.rand(100))


# In[4]:

x = np.linspace(0, 2*np.pi, 300)
y = np.sin(x)
plt.plot(x, y)


# In[5]:

y2 = np.sin(x**2)
plt.plot(x, y, label=r'$\sin(x)$')
plt.plot(x, y2, label=r'$\sin(x^2)$')
plt.title('Some functions')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend();


# In[6]:

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)
plt.plot(x, y, linewidth=2);


# In[7]:

# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)

# example variable error bar values
yerr = 0.1 + 0.2*np.sqrt(x)
xerr = 0.1 + yerr

# First illustrate basic pyplot interface, using defaults where possible.
plt.figure()
plt.errorbar(x, y, xerr=0.2, yerr=0.4)
plt.title("Simplest errorbars, 0.2 in x, 0.4 in y");


# In[8]:

x = np.linspace(-5, 5)
y = np.exp(-x**2)
plt.semilogy(x, y);


# In[9]:

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
# This will put a text fragment at the position given:
plt.text(55, .027, r'$\mu=100,\ \sigma=15$', fontsize=14)
plt.axis([40, 160, 0, 0.03])
plt.grid(True)


# In[ ]:



