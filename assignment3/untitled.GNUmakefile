# 
# Makefile to automate some work with assigment 3
#
# Usage:
#     make test     # runs all your progamms, compares their output to sample output
#     make zip      # prepares a zip file of all your programs
#     make download # download sample data again
#
# your netid is used to create the zip file
#


NETID = jx624

test:
	@echo "Running all programs. There should be NO output from diff if everything is correct"
	python problem1.py sample_data_problem_1.txt > real_output_problem_1.txt
	diff real_output_problem_1.txt sample_output_problem_1.txt
	python problem2.py sample_data_problem_2.txt > real_output_problem_2.txt
	diff real_output_problem_2.txt sample_output_problem_2.txt
	python problem3.py sample_data_problem_3_1.txt sample_data_problem_3_2.txt > real_output_problem_3.txt
	diff real_output_problem_3.txt sample_output_problem_3.txt
	python problem4.py sample_data_problem_4.txt > real_output_problem_4.txt
	diff real_output_problem_4.txt sample_output_problem_4.txt
	python problem5.py sample_data_problem_5.txt > real_output_problem_5.txt
	diff real_output_problem_5.txt sample_output_problem_5.txt
	python problem6.py sample_data_problem_6.txt > real_output_problem_6.txt
	diff real_output_problem_6.txt sample_output_problem_6.txt
	python problem7.py sample_data_problem_7.txt > real_output_problem_7.txt
	diff real_output_problem_7.txt sample_output_problem_7.txt
	python problem8.py sample_data_problem_8.txt > real_output_problem_8.txt
	diff real_output_problem_8.txt sample_output_problem_8.txt

zip:
	zip $(NETID)_assignment_3.zip problem?.py 

download:
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_data_problem_1.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_output_problem_1.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_data_problem_2.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_output_problem_2.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_data_problem_3_1.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_data_problem_3_2.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_output_problem_3.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_data_problem_4.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_output_problem_4.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_data_problem_5.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_output_problem_5.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_data_problem_6.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_output_problem_6.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_data_problem_7.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_output_problem_7.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_data_problem_8.txt
	wget -N  http://vgc.poly.edu/projects/gx5003-fall2014/week3/lab/data/sample_output_problem_8.txt