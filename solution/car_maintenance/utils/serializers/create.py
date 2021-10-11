def create_update_object_serializer(
    Serializer_class, data, instance=None, partial=True
):
    serializer = Serializer_class(data=data, instance=instance, partial=partial)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer
