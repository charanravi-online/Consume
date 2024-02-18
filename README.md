# ⚠️ WARNING 

When consume.py is run, a complex calculation is performed which utilises around 2TB of system RAM.
Some of the basic operations are temporarily down since the demand for RAM would be so high. 
Any normal user in their right mind would not have over 2TB of RAM installed, so use this with caution.
Although not harmful, it may cause some damage to the system and I take no reponsibility for it.
This is for research and education purpose only. Use it at your own risk.

# Consume

A simple project that consumes a lot of memory

## Description

For data = np.random.rand(2^48), the code generates an array with 2^48 random numbers between 0 and 1 using NumPy. The memory consumption can be calculated based on the size of each element in the array.

Assuming the default data type is 64-bit floating-point numbers (8 bytes per element in NumPy), the total memory consumption would be:

(2^48 elements) * (8 bytes/element) = 2^51 bytes

This corresponds to 2^41 gigabytes, or approximately 2 terabytes.

## Getting Started

### Dependencies

* numpy==1.26.4
* psutil==5.9.8

### Installing

* clone this repository
* install requirements.txt
```
pip install -r requirements.txt
```

### Executing program

When the requirements are installed, run the python file consume.py
```
python consume.py
```

## Help
In some cases you would need admin permission to run this file.

## Authors

[Charan](https://twitter.com/PyCharan)

## Version History

* 0.1
    * Initial Release

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [DomPizzie](https://gist.github.com/DomPizzie/7a5ff55ffa9081f2de27c315f5018afc)