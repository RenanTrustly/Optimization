# Optimization

Function to reduce the memory consumption of a pandas dataset.

It will iterate over the column types and reduce the default memory allocation. Example: in columns of type int64 it will check the reduction to the lowest level necessary for the data set and, in the worst case, reduce it by half, transforming it into an int32.

The function acts on integer, float and object columns. In the case of an object, if the number of unique information is less than 50% of the number of observations, then the column will be changed to the "categorical" type.

Hope you like it =)
