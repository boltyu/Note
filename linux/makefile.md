### @
    @cp "no echo"

### special macro
    $@ the name of the file to be made
    $/ the name of the changed dependents
    $< the name of the related file that caused the action
    $* the prefix shared by target and dependent files

    ```makefile example
    $(TARGET): sample.o sample_comm_vdec.o sample_comm_vcodec.o
	$(CXX) $(CFLAGS) $(LDFLAGS) -o $@ sample.o sample_comm_vdec.o sample_comm_vcodec.o $(LDLIBS)

    sample.o: sample.cpp
        $(CXX) $(CFLAGS) $(LDFLAGS) -c $< $(LDLIBS)

    sample_comm_vcodec.o: sample_comm_vcodec.cpp
        $(CXX) $(CFLAGS) $(LDFLAGS) -c $< $(LDLIBS)

    sample_comm_vdec.o: $(COMM_SAMPLE_DIR)/sample_comm_vdec.c
        $(CC) $(CFLAGS) $(LDFLAGS) -c $< $(LDLIBS)
    ```