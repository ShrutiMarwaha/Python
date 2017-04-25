# Arbitrary Argument Lists. The syntax is the * and **. The names *args and **kwargs are only by convention but there's no hard requirement to use them.

# use *args when you're not sure how many arguments might be passed to your function
def print_everything(*args):
        for count, thing in enumerate(args):
            print('{0}. {1}'.format(count, thing))

print ("use of *args:")
print_everything('apple', 'banana', 'cabbage', 'tomato')


# **kwargs allows you to handle named arguments that you have not defined in advance
def table_things(**kwargs):
    for name, value in kwargs.items():
        print( '{0} = {1}'.format(name, value))

print ('\nuse of **kwargs:')
table_things(apple = 'fruit', cabbage = 'vegetable', rose = 'flower')

def fetch_vcf_names(*args):
    return args

print (fetch_vcf_names('a','b','c'))
#print (fetch_vcf_names('669192-UDN671572-P_HVV7TBCXX-2-ID06.all.nomultiallelic_and_indelsnorm.reheader.vcf.gz', '669181-UDN406801-D_HVV7TBCXX-2-ID08.all.nomultiallelic_and_indelsnorm.reheader.vcf.gz'))


