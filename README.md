# libff_init
initialisation code generator in Python for `Fp_model` class from scipr [libff](https://github.com/scipr-lab/libff) C++ finite field library 

Usage:
```python
import libff_field_init

# Let's initialize GF(p), with p prime:
p = 1173927494001644411490688634382421854730749054815252052864119

iv = libff_field_init.compute_init_vals(p)
libff_field_init.pprint(iv,'my_finite_field')
```

Result: (generated C++11 code)
```cpp
auto modulus = bigint<static_cast<mp_size_t>(4)>("1173927494001644411490688634382421854730749054815252052864119");
my_finite_field::euler = bigint<static_cast<mp_size_t>(4)>("586963747000822205745344317191210927365374527407626026432059");
my_finite_field::t = bigint<static_cast<mp_size_t>(4)>("586963747000822205745344317191210927365374527407626026432059");
my_finite_field::t_minus_1_over_2 = bigint<static_cast<mp_size_t>(4)>("293481873500411102872672158595605463682687263703813013216029");
my_finite_field::Rsquared = bigint<static_cast<mp_size_t>(4)>("665490534691955392035634198969021676234406366821756662718595");
my_finite_field::Rcubed = bigint<static_cast<mp_size_t>(4)>("846723108556286790014337525304393905511498315677001073438544");
my_finite_field::s = 1;
my_finite_field::num_bits = 200;
my_finite_field::inv = 6631491265930121913UL;
```
