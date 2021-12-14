   # for i in range(len(corners)):
    #         for j in range(i+1,len(corners)):
    #                 corner1=tuple(corners[i][0])
    #                 corner2=tuple(corners[j][0]) # since corners if of list form convert to tuple

    #                 color=tuple(map(lambda x: int(x),np.random.randint(0,255,size=3)))
    #                         # lowerBound, higherBound , number of random samples to pick
    #                         # numpy has 32,64 bit integers but python uses 8 bit integer need to convert to python compatabile, also randint() returns list convert that
    #                         # 2.Instead of the map(lambda... for the np.random.randint you can also tuple a comprehension for the function.
    #                                 #  color = tuple(int(x) for x in np.random.randint())
    #                         # 3. Just in case you're not a fan of the map function, try:
    #                                 # color = [int(x) for x in np.random.randint(0, 255, size=3)]
    #         cv2.line(img,corner1,corner2,color,1)
    #         # indenting it inner for every corner line make
    #                         # indenting this line separately to make 1 point to many etc...
