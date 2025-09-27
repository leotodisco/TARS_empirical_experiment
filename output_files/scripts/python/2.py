def get_meteor_id(obj_or_model, obj_pk=None):
    """Return an Alea ID for the given object."""
    if obj_or_model is None:
        return None
    # Django model._meta is now public API -> pylint: disable=W0212
    meta = obj_or_model._meta
    model = meta.model
    if model is ObjectMapping:
        # this doesn't make sense - raise TypeError
        raise TypeError("Can't map ObjectMapping instances through self.")

    # try getting value of AleaIdField straight from instance if possible
    if isinstance(obj_or_model, model):
        # obj_or_model is an instance, not a model.
        if isinstance(meta.pk, AleaIdField):
            return obj_or_model.pk
        if obj_pk is None:
            # fall back to primary key, but coerce as string type for lookup.
            obj_pk = str(obj_or_model.pk)
    alea_unique_fields = [
        field
        for field in meta.local_fields
        if isinstance(field, AleaIdField) and field.unique
    ]
    if len(alea_unique_fields) == 1:
        # found an AleaIdField with unique=True, assume it's got the value.
        aid = alea_unique_fields[0].attname
        if isinstance(obj_or_model, model):
            val = getattr(obj_or_model, aid)
        elif obj_pk is None:
            val = None
        else:
            val = model.objects.values_list(aid, flat=True).get(
                pk=obj_pk,
            )
        if val:
            return val

    if obj_pk is None:
        # bail out if args are (model, pk) but pk is None.
        return None

    # fallback to using AleaIdField from ObjectMapping model.
    content_type = ContentType.objects.get_for_model(model)
    try:
        return ObjectMapping.objects.values_list(
            'meteor_id', flat=True,
        ).get(
            content_type=content_type,
            object_id=obj_pk,
        )
    except ObjectDoesNotExist:
        return ObjectMapping.objects.create(
            content_type=content_type,
            object_id=obj_pk,
            meteor_id=meteor_random_id('/collection/%s' % meta),
        ).meteor_id