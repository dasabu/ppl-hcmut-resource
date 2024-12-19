.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field static a I

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
	iconst_1
	putstatic BKoolClass/a I
Label1:
	return
.limit stack 1
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is d I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is e I from Label0 to Label1
	iconst_1
	istore_2
	bipush 100
	istore_1
	bipush 20
	istore_2
	iload_2
	ineg
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 3
.limit locals 3
.end method
