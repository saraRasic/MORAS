Require Import Bool.

Notation "! a" := (negb a) (at level 10).

(*1.a*)
Goal forall (x y : bool),
  (x && !y) || (!x && !y) || (!x && y) = !x || !y.
Proof.
 intros. destruct x, y.
  - simpl. reflexivity.
  - simpl. reflexivity.
  - simpl. reflexivity.
  - simpl. reflexivity.
Qed.

(*1.b*)
Goal forall X Y Z,
  ~(~X /\ Y /\ Z) /\ ~(X /\ Y /\ Z) /\ (X /\ ~Y /\ Z) <-> X /\ ~Y /\ Z.
Proof.
 intros X Y Z. split.
  - intros x. destruct x. destruct H0. assumption.
  - intros x. destruct x. destruct H0. split.
    -- intros A. apply A. exact H.
    -- split.
       --- intros h. destruct h. destruct H3. apply H0. exact H3.
       --- split.
           + exact H.
           + split.
             ++ exact H0.
             ++ exact H1.
Qed.

