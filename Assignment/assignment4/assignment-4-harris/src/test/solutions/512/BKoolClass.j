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
.var 1 is b [I from Label0 to Label1
	iconst_2
	newarray int
	dup
	iconst_0
	sipush 1200
	iastore
	dup
	iconst_1
	sipush 200
	iastore
	astore_1
	iconst_1
	ifle Label2
Label3:
	aload_1
	iconst_0
	iaload
	invokestatic io/writeInt(I)V
Label4:
	goto Label5
Label2:
Label6:
	aload_1
	iconst_1
	iaload
	invokestatic io/writeInt(I)V
Label7:
Label5:
Label1:
	return
.limit stack 6
.limit locals 2
.end method
