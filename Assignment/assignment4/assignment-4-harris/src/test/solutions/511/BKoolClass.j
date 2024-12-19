.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is n1 I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is n2 I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is n3 I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is i I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is count I from Label0 to Label1
	bipush 10
	istore 5
	iload_1
	invokestatic io/writeInt(I)V
	iload_2
	invokestatic io/writeInt(I)V
	iconst_2
	istore 4
Label2:
	iload 4
	iload 5
	iconst_1
	isub
	if_icmpgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
Label6:
	iload_1
	iload_2
	iadd
	istore_3
	iload_3
	invokestatic io/writeInt(I)V
	ldc "  "
	invokestatic io/writeStr(Ljava/lang/String;)V
	iload_2
	istore_1
	iload_3
	istore_2
Label7:
	iload 4
	iconst_1
	iadd
	istore 4
	goto Label2
Label3:
Label1:
	return
.limit stack 6
.limit locals 6
.end method
