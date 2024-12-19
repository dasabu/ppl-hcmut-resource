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

.method public foo()I
Label0:
.var 0 is this LBKoolClass; from Label0 to Label1
	bipush 100
	ireturn
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is bk LBKoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_1
.var 2 is spkt LBKoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_2
.var 3 is zoo I from Label0 to Label1
	aload_1
	invokevirtual BKoolClass/foo()I
	istore_3
	iload_3
	aload_2
	invokevirtual BKoolClass/foo()I
	iadd
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 2
.limit locals 4
.end method
