.source BKoolClass.java
.class public BKoolClass
.super java.lang.Object
.field total [I
.field name Ljava/lang/String;

.method public <init>()V
.var 0 is this LBKoolClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_4
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	putfield BKoolClass/total [I
Label1:
	return
.limit stack 5
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
.var 1 is bk LBKoolClass; from Label0 to Label1
	new BKoolClass
	dup
	invokespecial BKoolClass/<init>()V
	astore_1
	aload_1
	getfield BKoolClass/total [I
	iconst_0
	bipush 9
	iastore
	aload_1
	getfield BKoolClass/total [I
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
	aload_1
	getfield BKoolClass/total [I
	iconst_1
	iaload
	invokestatic io/writeInt(I)V
	aload_1
	getfield BKoolClass/total [I
	iconst_2
	iaload
	invokestatic io/writeInt(I)V
	aload_1
	getfield BKoolClass/total [I
	iconst_3
	iaload
	invokestatic io/writeInt(I)V
Label1:
	return
.limit stack 7
.limit locals 2
.end method
