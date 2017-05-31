def i4mat_write(output_filename,m,n,input_file):

    #An I4MAT is an array of I4's.

    """Parameters:

    Input, string OUTPUT_FILENAME, the output filename.

    Input, integer M, the spatial dimension.
    
    Input, integer N, the number of points.

    Input, integer TABLE(M,N), the points."""

    #Open the file
    output=open(output_filename,'w')
    for j in range(n):
        for i in range(m):
            k='%d' %input_file[i,j]
            output.write(k)
        output.write('\n')
        output.close()
        return output
    
