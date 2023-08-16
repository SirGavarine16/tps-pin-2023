# Generation of Spam Database

Table 1 -> src, dst, tmsp
Table 2 -> dst, tmsp, is_spam

Result:
Table 3 -> dst, src, spam_count

## Business Logic

create table 3

For each element in Table 2
	if is marked as spam:
		find source by comparing destination and timestamp
		if source is found:
			if is registered update count otherwise create record
