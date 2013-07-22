	.file	"garbage.c"
	.section	.rodata
.LC0:
	.string	"%d/%d = %f\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$64, %esp
	movl	12(%ebp), %eax
	addl	$4, %eax
	movl	(%eax), %eax
	movl	%eax, (%esp)
	call	atoi
	movl	%eax, 52(%esp)
	movl	12(%ebp), %eax
	addl	$8, %eax
	movl	(%eax), %eax
	movl	%eax, (%esp)
	call	atoi
	movl	%eax, 56(%esp)
	movl	52(%esp), %eax
	movl	%eax, %edx
	sarl	$31, %edx
	idivl	56(%esp)
	movl	%eax, 44(%esp)
	fildl	44(%esp)
	fstps	60(%esp)
	flds	60(%esp)
	movl	$.LC0, %eax
	fstpl	12(%esp)
	movl	56(%esp), %edx
	movl	%edx, 8(%esp)
	movl	52(%esp), %edx
	movl	%edx, 4(%esp)
	movl	%eax, (%esp)
	call	printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 4.6.3-1ubuntu5) 4.6.3"
	.section	.note.GNU-stack,"",@progbits
